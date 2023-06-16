# Weather Tracker App

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/berkcohadar/weather_tracker.git
$ cd weather_tracker
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
$ cd weather_tracker
$ python manage.py runserver
```
And navigate to `http://localhost:8000/`.

## HOW-TO

### How to Create an App in Django ?

Django is famous for its unique and fully managed app structure. For every functionality, an app can be created like a completely independent module.

To create a basic app in your Django project you need to go to the directory containing manage.py and from there enter the command

```sh
$ python manage.py startapp APP_NAME
```
OR
```sh
$ django-admin startapp APP_NAME
```

This will create a django application. Now you will see a newly-created folder called APP_NAME. This folder will include everything that associates with your new application.

To include this new app in your django app, you need to go the `settings.py` folder. Then, you need to add your newly-created app as `"APP_NAME"` to the `INSTALLED_APPS` array defined in `settings.py` folder.

```
# settings.py

INSTALLED_APPS = [
    ...
    "APP_NAME",
]

```

### How to Create a Model in Django ?

Once you've created an app, you can create its models. To do that, you should first go into your newly-created app's folder. Under this folder, you will find a file named `models.py`. Inside this file, you should include your models.

Django models can easily be implemented as the same way as Python classes. The only difference is that your models need to inherit `django.db.models.Model`. See example below.

```
# APP_NAME/models.py

from django.db import models

class ExampleModel(models.Model):
    # Your Model fields here.
    some_string = models.CharField()
    some_integer = models.IntegerField()
    some_date = models.DateField()

```

### How to Build a REST API Service in Django ?

A REST API is a standardized way to provide data to other applications. Those applications can then use the data however they want. Sometimes, APIs also offer a way for other applications to make changes to the data.

There are a few key options for a REST API request:

- GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
- POST — Creates a new record that gets appended to the database
- PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
- DELETE — Deletes the record at the given URI
- PATCH — Update individual fields of a record

#### Serialize the model

Serializers allow complex data such as querysets and model instances to be converted to native datatypes that can then be easily rendered into JSON, XML or other content types.

The serializer below will parse the queryset and return a JSON content with specific parameters for each object. These parameters are 'some_string', 'some_integer', and 'some_date'.

```
# APP_NAME/serializers.py

from rest_framework import serializers
from .models import ExampleModel

class ExampleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExampleModel
        fields = (
            'some_string',
            'some_integer',
            'some_date',
        )

```

#### Create views for your API
A view function, or view for short, is a Python function that takes a web request and returns a web response. This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or a data queryset.

For example, Let's assume we need to render each ExampleModel objects in JSON format.

To do so, we need to:

1. Query the database for all Model instances.
2. Pass that database queryset into the serializer we just created, so that it gets converted into JSON and rendered.

```
# APP_NAME/views.py

from rest_framework import viewsets

from .serializers import ExampleModelSerializer
from .models import ExampleModel

class ExampleModelViewSet(viewsets.ModelViewSet):
    queryset = ExampleModel.objects.all().order_by('name')
    serializer_class = ExampleModelSerializer

```

`ModelViewSet` is a special view that Django Rest Framework provides. It will handle GET and POST for Heroes without us having to do any more work.


#### Create URL Endpoints for your API service
This step is to point a URL at the viewset we just created.

In Django, URLs get resolved at the project level first. So there’s a file in the top directory called urls.py. In this file, you’ll see the URL for the admin site and all other installed apps. So, every time we've created a new model, we need to include its URLs to this file. Otherwise, we will not be able to reach any of the APIs we create inside this newly-created model.

```
# urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/app_name', include('APP_NAME.urls')),
    # YOUR NEW PATHS HERE
 ]
```

The code above, will include each API endpoint below.

```
# APP_NAME/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ExampleModelViewSet)
]
```