## Quickstart

```
# will build and run the web and db containers
docker-compose up -d
# will create the initial tables (roles and users)
docker-compose run web python manage.py db upgrade
# create a superuser
docker-compose run web python manage.py create_superuser user@domain.com us3rPassword
# enjoy -> http://<your-docker-ip>:5001
```

## Customize

