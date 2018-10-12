import argparse
import dateutil.parser as dp 
from is_wire.core import Message, Logger
from utils import get_pb_image, StreamChannel
from cv2 import VideoCapture, CAP_PROP_FPS
from sys import exit


def span_duration_ms(span):
    dt = dp.parse(span.end_time) - dp.parse(span.start_time)
    return dt.total_seconds() * 1000.0

service_name = 'CameraGateway.Frame'
log = Logger(name=service_name)

parser = argparse.ArgumentParser(
    description='Utility to capture a sequence of images from multiples cameras'
)
parser.add_argument(
    '--id', '-i', type=int, required=False, help='Camera ID', default=0)
parser.add_argument(
    '--device', '-d', type=int, required=False, help='Camera device. 0 for /dev/video0', default=0)
parser.add_argument(
    '--fps', '-f', type=int, required=False, help='FPS', default=10)
parser.add_argument(
    '--uri', '-u', type=str, required=False, help='broker_uri', default='amqp://localhost:5672')
args = parser.parse_args()

device = args.device
fps = args.fps
broker_uri = args.uri

cap = VideoCapture(device)
if cap.isOpened():
    log.info('Connected to device: /dev/video{}'.format(device))
else:
    log.error('Coudn\'t find device: /dev/video{}'.format(device))
    exit()

log.info('Camera FPS set to {}'.format(fps))
cap.set(CAP_PROP_FPS, fps)

channel = StreamChannel(broker_uri)
log.info('Connected to broker {}', broker_uri)

log.info('Starting to capture')

while True:
    ret, frame = cap.read()

    msg = Message()
    msg.topic = 'CameraGateway.{}.Frame'.format(args.id)
    msg.pack(get_pb_image(frame))
    channel.publish(msg)

