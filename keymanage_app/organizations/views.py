from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import OrganizationForm, KeysForm, KeysBlockForm
from .models import Organization, Keys
from django.views.generic import UpdateView, DeleteView, ListView


def index(request):
    return render(request, 'organizations/index.html')


def organizations(request):
    org = Organization.objects.all()
    return render(request, 'organizations/orgs.html', {'orgs': org})


def keys(request):
    key = Keys.objects.all()
    org = Organization.objects.all()
    context = {
        'keys': key,
        'orgs': org,
    }
    return render(request, 'organizations/keys.html', context)


def add_org(request):
    error = ''
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizations')
        else:
            error = 'Данные были введены неверно'
    form = OrganizationForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'organizations/add_org.html', context)


def add_key(request):
    org = Organization.objects.all()
    error = ''
    if request.method == 'POST':
        form = KeysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('keys')
        else:
            error = 'Данные были введены неверно'
    form = KeysForm()
    context = {
        'form': form,
        'error': error,
        'orgs': org,
    }
    return render(request, 'organizations/add_key.html', context)


def filter_key(request, id_org):
    key = Keys.objects.filter(id_org_id=id_org)
    org = Organization.objects.all()
    context = {
        'keys': key,
        'orgs': org,
    }
    return render(request, 'organizations/filter_key.html', context)


class UpdateKeyBlock(UpdateView):
    model = Keys
    template_name = "organizations/update_keyblock.html"
    form_class = KeysBlockForm


class UpdateOrg(UpdateView):
    model = Organization
    template_name = "organizations/update_org.html"
    form_class = OrganizationForm


class DeleteOrg(DeleteView):
    model = Organization
    template_name = "organizations/delete_org.html"
    success_url = '/organizations/'


class UpdateKey(UpdateView):
    model = Keys
    template_name = "organizations/update_key.html"
    form_class = KeysForm
    orgs = Organization.objects.all()


class DeleteKeys(DeleteView):
    model = Keys
    template_name = "organizations/delete_key.html"
    success_url = '/keys/'
