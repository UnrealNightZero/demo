from django.db import models

class USER_DATA(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    address = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(max_length=254, db_index=True)
    phone = models.CharField(max_length=20, db_index=True)

