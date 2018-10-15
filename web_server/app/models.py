# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class PhotoAlbum(models.Model):
    name = models.CharField(max_length=64)
    point = models.CharField(max_length=64)
    createTime = models.CharField(max_length=128)
    count = models.ImageField(null=True)


class Picture(models.Model):
    file = models.ImageField(upload_to="rec/picture/%m%d")
    size = models.IntegerField()
    name = models.CharField(max_length=64)
    point = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    album = models.ForeignKey(PhotoAlbum, related_name="album", null=True)


class Media(models.Model):
    file = models.ImageField(upload_to="rec/media/%m%d")
    size = models.IntegerField()
    name = models.CharField(max_length=64)
    point = models.CharField(max_length=64)
    duration = models.IntegerField(null=True)
    date = models.CharField(max_length=64)
    title = models.CharField(max_length=64, null=True)
