from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Section,Intro
from django.shortcuts import render
# Create your views here.

def index(request):
	content_list = Section.objects.order_by("number_in_set")
	#template = loader.get_template("options/index.html")
	introduction = Intro.objects.order_by("number_in_set")
	context = {"content_list": content_list,
				"introduction": introduction}
	return render(request, "options/index.html", context)
