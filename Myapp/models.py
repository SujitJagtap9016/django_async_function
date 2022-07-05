from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

# In this models.py file date databse comunnicate to our project.
# we need to create model and connect our code which we written in views.py file
# Manage.py file access the date from templeted through the help of views.py file and store into database.
# In this models.py file I have created the default App name model that is Myapp
# here the call define the model 

class Myapp(models.Model):
  pass

