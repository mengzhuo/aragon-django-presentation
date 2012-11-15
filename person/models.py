# -*- coding: utf-8 -*-s

from django.db import models

# Create your models here.

class Person( models.Model ):
    
    name = models.CharField(max_length=8,
                            verbose_name=u'用户名'
                            )
    follow = models.ManyToManyField(
                     'self', related_name = 'follower',
                    symmetrical=False,blank=True,null=True)

    def __unicode__(self):
        return self.name
