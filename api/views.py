# Create your views here.

# -*- coding: utf-8 -*-


from django.shortcuts import render_to_response

def test_static(request):
    return render_to_response('testmap.html',{})
