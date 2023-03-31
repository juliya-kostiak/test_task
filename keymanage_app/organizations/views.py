from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Organization, Keys
from django.views.decorators.http import require_http_methods


def index(request):
    return render(request, 'organizations/index.html')


def organizations(request):
    org = Organization.objects.all()
    return render(request, 'organizations/orgs.html', {'orgs': org})


def keys(request):
    key = Keys.objects.all()
    org = Organization.objects.all()
    return render(request, 'organizations/keys.html', {'keys': key, 'orgs': org})


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



