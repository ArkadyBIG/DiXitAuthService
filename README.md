# DiXit Auth Server
## Building image
To build docker image, use command:
```bash
docker build --tag dixit_auth .
```

------

## Run container on local machine

To run container and access 

``` bash
docker run --rm -it -p 8083:8083  dixit_auth
```

### Supported requests

| URL | Method | Params |
| :---------------| :------------------| :---------------|
| http://0.0.0.0:8083/authorize        | Post| `{ "user_id": 123 }`|
| http://0.0.0.0:8083/getByToken    | Get | `{ "token": "7847838381274000"}`|

