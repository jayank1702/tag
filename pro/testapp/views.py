from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from testapp.forms import RegisterForm
from django.http import HttpResponseRedirect
from django.db import models
from testapp.models import Resident,Visitor,Worker,Delivery,Company

# Create your views here.
@login_required
def my_dashboard(request):
    return render (request,'testapp/dashboard.html')

def register_view(request):
    form=RegisterForm
    if request.method=="POST":
        form=RegisterForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request,'testapp/register.html',{'form':form})

def home_page_view(request):
    return render(request,'testapp/home.html')


def aboutus_view(request):
    return render(request,'testapp/aboutus.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
# Create your views here.


class ResidentListView(ListView):
    model=Resident


class ResidentCreateView(CreateView):
    model=Resident
    fields='__all__'


class ResidentDetailView(DetailView):
    model=Resident


class ResidentUpdateView(UpdateView):
    model=Resident
    fields='__all__'


class ResidentDeleteView(DeleteView):
    model=Resident
    success_url=reverse_lazy('home')


class WorkerListView(ListView):
    model=Worker


class WorkerCreateView(CreateView):
    model=Worker
    fields='__all__'


class WorkerDetailView(DetailView):
    model=Worker


class WorkerUpdateView(UpdateView):
    model=Worker
    fields='__all__'


class WorkerDeleteView(DeleteView):
    model=Worker
    success_url=reverse_lazy('home')


class VisitorListView(ListView):
    model=Visitor


class VisitorCreateView(CreateView):
    model=Visitor
    fields='__all__'


class VisitorDetailView(DetailView):
    model=Visitor


class VisitorUpdateView(UpdateView):
    model=Visitor
    fields='__all__'


class VisitorDeleteView(DeleteView):
    model=Visitor
    success_url=reverse_lazy('home')

class DeliveryListView(ListView):
    model=Delivery


class DeliveryDetailView(DetailView):
    model=Delivery


class DeliveryCreateView(CreateView):
    model=Delivery
    fields='__all__'


class DeliveryDeleteView(DeleteView):
    model=Delivery
    success_url=reverse_lazy('home')


class DeliveryUpdateView(UpdateView):
    model=Delivery
    fields='__all__'


class CompanyListView(ListView):
    model=Company


class CompanyDetailView(DetailView):
    model=Company
    
class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('home')


class CompanyUpdateView(UpdateView):
    model=Company
    fields='__all__'

class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'
