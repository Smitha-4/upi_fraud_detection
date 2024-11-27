from django.db import models

# Create your models here.
def results(request):
    if ('Post'==True):
        phone_number = request.get('phone_number')