# is-webcam

## Prepare environment

In order to send/receive messages an amqp broker is necessary, to create one simply run:

```sh
docker container run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

## Publishing the default camera:

```sh
docker container run --rm -d \
  --device=/dev/video0 \
  --memory=60M \
  --network=host \
  --name is-webcam \
    hsneto/is-webcam:1.2 \
    python3 stream.py
```

## Publishing another webcam:

```sh
docker container run --rm -d \
  --device=/dev/video1 \
  --memory=60M \
  --network=host \
  --name is-webcam \
    hsneto/is-webcam:1.2 \
    python3 stream.py --device 1
```


