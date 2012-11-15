# Create your views here.

from django.http import HttpResponse

from person.models import Person

def show( request, name ):
    who = Person.objects.get(name=name)
    tweets = who.tweet.all()[0].content
    #import ipdb; ipdb.set_trace()
    return HttpResponse("%s:%s" % (who, tweets))
