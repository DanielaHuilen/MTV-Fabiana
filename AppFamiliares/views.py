from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familia(request):
    
    integrante1=Familiares(nombre="German", edad=30, cumpleanos=("1992-6-10"))
    
    integrante2=Familiares(nombre="Daniela", edad=33, cumpleanos="1989-1-31")
    
    integrante3=Familiares(nombre="Angela", edad=89, cumpleanos="1933-11-20")
    
    integrante1.save()
    integrante2.save()
    integrante3.save()
    
    template=loader.get_template("familiar.html")
    
    context= {"familiar": [integrante1,integrante2,integrante3]}
    
    document=template.render(context)
    return HttpResponse(document)

