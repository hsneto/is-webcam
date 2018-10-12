# is-webcam

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


