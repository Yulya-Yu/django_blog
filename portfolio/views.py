from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Project


# Create your views here.



def project_list(request):
    
    project = Project.objects.all()
    context = {
    'project': project
  }
    return render(request, 'portfolio/project_list.html', context)

def project_detail(request, slug):
	# return HttpResponse(slug)
	project = Project.objects.get(slug=slug)
	return render(request, 'portfolio/project_detail.html', {'project': project})