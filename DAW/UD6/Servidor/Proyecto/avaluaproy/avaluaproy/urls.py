"""avaluapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from common import views as common_views
from core import views as core_views
from programacion_didactica import views as programacion_didactica_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),
    path('modulo_list/', core_views.ModuloListView.as_view(), name='modulo_list'),
    path('modulo_detail/<int:pk>/', core_views.ModuloDetailView.as_view(), name='modulo_detail'),
    path('ra_list/', core_views.RAListView.as_view(), name='ra_list'),
    path('ra_detail/<int:pk>/', core_views.RADetailView.as_view(), name='ra_detail'),
    path('ce_list/', core_views.CEListView.as_view(), name='ce_list'),
    path('ce_detail/<int:pk>/', core_views.CEDetailView.as_view(), name='ce_detail'),
    #UD6.7.b BEGIN
    path('unidad_list/', programacion_didactica_views.UnidadListView.as_view(), name='unidad_list'),
    path('unidad_detail/<int:pk>/', programacion_didactica_views.UnidadDetailView.as_view(), name='unidad_detail'),
    path('ie_list/', programacion_didactica_views.InstEvListView.as_view(), name='ie_list'),
    path('ie_detail/<int:pk>/', programacion_didactica_views.InstEvDetailView.as_view(), name='ie_detail'),
    path('pond_ra_list/', programacion_didactica_views.PondRAListView.as_view(), name='pond_ra_list'),
    path('pond_ra_detail/<int:pk>/', programacion_didactica_views.PondRADetailView.as_view(), name='pond_ra_detail'),
    path('pond_ce_list/', programacion_didactica_views.PondCritListView.as_view(), name='pond_ce_list'),
    path('pond_ce_detail/<int:pk>/', programacion_didactica_views.PondCritDetailView.as_view(), name='pond_ce_detail'),
    path('pond_ce_ud_list/', programacion_didactica_views.PondCritUDListView.as_view(), name='pond_ce_ud_list'),
    path('pond_ce_ud_detail/<int:pk>/', programacion_didactica_views.PondCritUDDetailView.as_view(), name='pond_ce_ud_detail'),
    #UD6.7.b END
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
