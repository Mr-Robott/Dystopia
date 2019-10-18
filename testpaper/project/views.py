from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .models import *

def login(request):
    pass

def register(request):
    pass

@login_required
def add_project(request):
    pass

@login_required
def edit_project(request):
    pass

@login_required
def delete_project(request):
    pass

@login_required
def filter_project():
    pass


