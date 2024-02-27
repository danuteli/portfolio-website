from django.shortcuts import render
from django.conf import settings
from .models import Project
import os
import markdown

# Create your views here.

# save path for content dir
content_path = settings.BASE_DIR + '/static/portfolio/content/'

# get list of projects in content dir
projects_titles = os.listdir(content_path)

# instantiate objects of the Project class for each project and save all in a list
projects = []

for title in projects_titles:
    files = os.listdir(content_path + title)
    media = [f for f in files if ".md" not in f]

    project = Project(title=title, filenames=media)
    projects.append(project)




def convertMarkdown(name):

    with open(settings.BASE_DIR + '/static/portfolio/content/' + name + '/' + name + '.md', 'r') as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content)
    return html_content


def index(request):

    return render (request, 'portfolio/index.html', {
        'projects': projects
    })


def project(request, name):

    find_project = next((project for project in projects if project.title == name), None)
    if find_project:
        return render(request, 'portfolio/project.html', {
            'project': find_project,
            'content': convertMarkdown(name)
        }) 
    else:
        return render(request, 'portfolio/error.html')
