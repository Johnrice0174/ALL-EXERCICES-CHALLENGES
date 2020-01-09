from django.db import models


class Streamingdata(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    video_vf = models.CharField(max_length=400, null=True)
    video_vo = models.CharField(max_length=400, null=True)

