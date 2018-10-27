from django.db import models


class TeamInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    post = models.CharField(max_length=128)
    description = models.CharField(max_length=512)

    src_img = models.CharField(max_length=256)
