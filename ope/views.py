# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render

def cadastro_disciplina(request):
    disciplina = get_template('cadastro_disciplinas.html')
    return HttpResponse(disciplina.render())