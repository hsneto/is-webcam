# is-webcam

```sh
docker container run --rm -d \
  --device=/dev/video0 \
  --memory=60M \
  --network=host \
  --name cam5 \
    hsneto/is-webcam:1.1
```
