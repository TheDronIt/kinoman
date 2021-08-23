from django.shortcuts import render
from .models import *

def index(requset):
	data = {

	}
	return render(requset, 'page/index.html', data)
