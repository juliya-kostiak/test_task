from django.shortcuts import render, redirect
from .models import Organization, Keys
from django.views.decorators.http import require_http_methods


def index(request):
    orgs = Organization.objects.all()
    keys = Keys.objects.all()
    return render(request, 'organizations/index.html', {'orgs': orgs, 'keys': keys})


@require_http_methods(['POST'])
def add_org(request):
    name = request.POST['title']
    org = Organization(name=name)
    org.save()
    return redirect('index')


def update_org(request, org_id, name):
    org = Organization.objects.get(id=org_id)
    org.name = Organization(name=name)
    org.save()
    return redirect('index')


def delete_org(request, org_id):
    org = Organization.objects.get(id=org_id)
    org.delete()
    return redirect('index')



