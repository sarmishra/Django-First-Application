# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    html_source_code = """
        <html>
        <title> Hello World </title>
            <body>
                <h1> Hello World </h1>
                <p> This is your first django hello world application  </p>
            </body>
        </html>
    """
    return HttpResponse(html_source_code) 
