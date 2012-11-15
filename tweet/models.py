# -*- coding: utf-8 -*-s

from django.db import models

from person.models import Person

# Create your models here.

class Tweet( models.Model ):
    
    user = models.ForeignKey(Person,
                            related_name = 'tweet',
                             )
                             
    content = models.CharField(max_length=140,
                               verbose_name=u'推文',
                               )

    def __unicode__(self):
        return u"%s的推文：%s" % (self.user.name, self.content)
