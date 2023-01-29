from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def projetos (request):
    return render(request, 'projetos.html')
