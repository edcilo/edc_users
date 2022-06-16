# Users microservice

## Local instalation

Clone repository
```
git clone git@github.com:GravitiMX/msAqUsers.git
```

Create .env file
```
cp .env.example .env
```
Modify env variables into the .env file

Build docker image with docker-compose
```
docker-compose build
```

Run docker-compose yaml and access to de flask image
```
docker-compose up -d
docker-compose exec ms_aq_users sh
```

Execute migrations
```
flask db stamp
flask db migrate
flask db upgrade
```

Execute seeders to populate database
```
flask seed run --root=./ms/db/seeders
```

Run tests
```
coverage run -m pytest
```
