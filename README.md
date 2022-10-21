# Carford in Django Rest Framework


## Steps
- run ```docker-compose up --build```

Once the docker is running, you can test the API below


### I'm sending an export of requestes from postman, file:
```advice_health.postman_collection.json```
just import to your postman and test API

I'm using basic auth for this assessment, 
username = admin
password = 123456

feel free to create another user, using ```createsuperuser``` command


## Added Test Cases with APITestCase
just run insde docker:
```python manage.py test```