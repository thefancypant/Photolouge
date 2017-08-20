# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
def hello(request,*args):
    context={"testname":args[0]}
    return render_to_response('testpage.html',context)
    #return  render_to_response('helloworld.html')
    #return HttpResponse()

