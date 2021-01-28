build

```podman build -t tube-map .```

to run locally

```podman run --rm -it -v $(pwd):/srv -p 8080:5000 tube-map flask run```
