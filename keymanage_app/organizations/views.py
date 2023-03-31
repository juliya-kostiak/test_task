from django.shortcuts import render, redirect
from .forms import OrganizationForm, KeysForm
from .models import Organization, Keys
from django.views.generic import UpdateView, DeleteView


def index(request):
    return render(request, 'organizations/index.html')


def organizations(request):
    org = Organization.objects.all()
    return render(request, 'organizations/orgs.html', {'orgs': org})


def keys(request):
    key = Keys.objects.all()
    org = Organization.objects.all()
    return render(request, 'organizations/keys.html', {'keys': key, 'orgs': org})


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


class UpdateOrg(UpdateView):
    model = Organization
    template_name = "organizations/update_org.html"
    form_class = OrganizationForm


class DeleteOrg(DeleteView):
    model = Organization
    template_name = "organizations/delete_org.html"
    success_url = '/organizations/'


class DeleteKeys(DeleteView):
    model = Keys
    template_name = "organizations/delete_key.html"
    success_url = '/keys/'









def delete_org(request, org_id):
    org = Organization.objects.get(id=org_id)
    org.delete()
    return redirect('index')



