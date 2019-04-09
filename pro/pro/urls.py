"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page_view,name='home'),
    url(r'^logout/',views.logout_view),
    url(r'^aboutus/',views.aboutus_view),
    url(r'^register/', views.register_view),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^dashboard/',views.my_dashboard),
    url(r'^residents/',views.ResidentListView.as_view(),name='resident'),
    url(r'^(?P<pk>\d+)/$',views.ResidentDetailView.as_view(),name='residentdetail'),
    url(r'^create/',views.ResidentCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$',views.ResidentUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$',views.ResidentDeleteView.as_view()),
    url(r'^visitors/',views.VisitorListView.as_view(),name='visitor'),
    url(r'^visitor/(?P<pk>\d+)/$',views.VisitorDetailView.as_view(),name='visitordetail'),
    url(r'^createvisitor/',views.VisitorCreateView.as_view()),
    url(r'^updatevisitor/(?P<pk>\d+)/$',views.VisitorUpdateView.as_view()),
    url(r'^deletevisitor/(?P<pk>\d+)/$',views.VisitorDeleteView.as_view()),
    url(r'^workers/',views.WorkerListView.as_view(),name='worker'),
    url(r'^worker/(?P<pk>\d+)/$',views.WorkerDetailView.as_view(),name='workerdetail'),
    url(r'^createworker/',views.WorkerCreateView.as_view()),
    url(r'^updateworker/(?P<pk>\d+)/$',views.WorkerUpdateView.as_view()),
    url(r'^deleteworker/(?P<pk>\d+)/$',views.WorkerDeleteView.as_view()),
    url(r'^companys/',views.CompanyListView.as_view(),name='company'),
    url(r'^company/(?P<pk>\d+)/$',views.CompanyDetailView.as_view(),name='companydetail'),
    url(r'^createcompany/',views.CompanyCreateView.as_view()),
    url(r'^updatecompany/(?P<pk>\d+)/$',views.CompanyUpdateView.as_view()),
    url(r'^deletecompany/(?P<pk>\d+)/$',views.CompanyDeleteView.as_view()),
    url(r'^deliverys/',views.DeliveryListView.as_view(),name='delivery'),
    url(r'^delivery/(?P<pk>\d+)/$',views.DeliveryDetailView.as_view(),name='deliverydetail'),
    url(r'^createdelivery/',views.DeliveryCreateView.as_view()),
    url(r'^updatedelivery/(?P<pk>\d+)/$',views.DeliveryUpdateView.as_view()),
    url(r'^deletedelivery/(?P<pk>\d+)/$',views.DeliveryDeleteView.as_view()),

    # url(r'^(?P<pk>\d+)/visitor/$',views.VisitorListView.as_view(),name='visitor'),
    # url(r'^(?P<pk>\d+)/detailvisitor/$',views.VisitorDetailView.as_view(),name='visitordetail'),

]
