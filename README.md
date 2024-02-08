# questioner_app

A Flask micro app allowing users to do CRUD operation on questions via RESTfull APIs endpoint and Swagger UI.

## Docker Quickstart

This app can be run completely using `Docker`

There are three main services:

To run the app

```bash
docker build -t questioner_app -f Dockerfile .
docker run -it -p 8080:8080 -t questioner_app
```

Go to `http://localhost:8080/api/v1/doc`. You will see a Swagger UI.

## TODO:
- Write Unitest for API
- Build POSTMAN collection for REST APIs
- Integrate RDS db
- Docker-compose for RDS and Flask service