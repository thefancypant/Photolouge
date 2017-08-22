# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Images(models.Model):
    imageId = models.IntegerField()
    imageType= models.CharField(max_length=10)

