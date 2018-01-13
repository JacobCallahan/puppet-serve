# puppet-serve
Host your own puppet module server

Clone this repo.

Modify the contents of 'modules' and build your image.

```
docker build -t puppet-serve .
```

Run the container and try it out, make sure to map the internal port to an external one.

```
docker run -p 1335:8080 puppet-serve
```