from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def membros(request):
    return render(request,'membros.html')