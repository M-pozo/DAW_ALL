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
#UD8.4
from django.urls import path, include
from django.views.generic import TemplateView

from common import views as common_views
from core import views as core_views
from programacion_didactica import views as programacion_didactica_views
from login import views as login_views
from rest_framework import routers
from core.api.views import *
from programacion_didactica.api.views import *
from programacion_aula.api.views import *


#UD10.3.a
router = routers.DefaultRouter()
#MODULO
router.register(r'modulo_list', ModuloListViewSet, basename='modulo_list')
router.register(r'modulo_detail', ModuloDetailViewSet, basename='modulo_detail')
#ResAprendizaje
router.register(r'ra_list', RAListViewSet, basename='ra_list')
router.register(r'ra_detail', RADetailViewSet, basename='ra_detail')
#CritEvaluacion
router.register(r'ce_list', CEListViewSet, basename='ce_list')
router.register(r'ce_detail', CEDetailViewSet, basename='ce_detail')

#Unidad
router.register(r'unidad_list', UnidadListViewSet, basename='unidad_list')
router.register(r'unidad_detail', UnidadDetailViewSet, basename='unidad_detail')
#InsEvaluacion
router.register(r'ie_list', IEListViewSet, basename='ie_list')
router.register(r'ie_detail', IEDetailViewSet, basename='ie_detail')
#PondRA
router.register(r'pond_ra_list', PondRAListViewSet, basename='pond_ra_list')
router.register(r'pond_ra_detail', PondRADetailViewSet, basename='pond_ra_detail')
#PondCE
router.register(r'pond_ce_list', PondCEListViewSet, basename='pond_ce_list')
router.register(r'pond_ce_detail', PondCEDetailViewSet, basename='pond_ce_detail')
#PondCEUD
router.register(r'pond_ce_ud_list', PondCEUDListViewSet, basename='pond_ce_ud_list')
router.register(r'pond_ce_ud_detail', PondCEUDDetailViewSet, basename='pond_ce_ud_detail')

#Alumno
router.register(r'alumno_list', AlumnoListViewSet, basename='alumno_list')
router.register(r'alumno_detail', AlumnoDetailViewSet, basename='alumno_detail')
#CriterioEvalUD
router.register(r'ce_ud_list', CEUDListViewSet, basename='ce_ud_list')
router.register(r'ce_ud_detail', CEUDDetailViewSet, basename='ce_ud_detail')
#CalificacionUDCE
router.register(r'cal_ud_ce_list', CalUDCEListViewSet, basename='cal_ud_ce_list')
router.register(r'cal_ud_ce_detail', CalUDCEDetailViewSet, basename='cal_ud_ce_detail')
#CalificacionCE
router.register(r'cal_ce_list', CalCEListViewSet, basename='cal_ce_list')
router.register(r'cal_ce_detail', CalCEDetailViewSet, basename='cal_ce_detail')
#CalificacionRA
router.register(r'cal_ra_list', CalRAListViewSet, basename='cal_ra_list')
router.register(r'cal_ra_detail', CalRADetailViewSet, basename='cal_ra_detail')
#CalificacionTotal
router.register(r'cal_total_list', CalTotalListViewSet, basename='cal_total_list')
router.register(r'cal_total_detail', CalTotalDetailViewSet, basename='cal_total_detail')

#UD7.2.b
urlpatterns = [
    #FRAMEWORK
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/calcular_nota/', CalcularNotasView.as_view(), name='api/calcular_nota'),

    #ADMIN
    path('admin/', admin.site.urls),

    #ALLAUTH UD8.4 BEGIN
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='common/home.html'), name='home'),
    #UD8.4 END 
    #LOGIN
    #UD8.2.a / UD8.2.b / UD8.2.c
    path('login/', login_views.LoginFormView.as_view(), name='login'),
    path('logout/', login_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    #common BEGIN
    path('', common_views.HomeView.as_view(), name='home'),
    path('panel/', common_views.PanelView.as_view(), name='panel'),
    #common END

    #core BEGIN
        #Modulo
            path('modulo_list/', core_views.ModuloListView.as_view(), name='modulo_list'),
            path('modulo_detail/<int:pk>/', core_views.ModuloDetailView.as_view(), name='modulo_detail'),
            path('modulo_create/', core_views.ModCreateView.as_view(), name='modulo_create'),
            path('modulo_update/<int:pk>/', core_views.ModUpdateView.as_view(), name='modulo_update'),
            path('modulo_delete/<int:pk>/', core_views.ModDeleteView.as_view(), name='modulo_delete'),
        #ResAprendizaje
            path('ra_list/', core_views.RAListView.as_view(), name='ra_list'),
            path('ra_detail/<int:pk>/', core_views.RADetailView.as_view(), name='ra_detail'),
            path('ra_create/', core_views.RACreateView.as_view(), name='ra_create'),
            path('ra_update/<int:pk>/', core_views.RAUpdateView.as_view(), name='ra_update'),
            path('ra_delete/<int:pk>/', core_views.RADeleteView.as_view(), name='ra_delete'),
        #CritEvaluacion
            path('ce_list/', core_views.CEListView.as_view(), name='ce_list'),
            path('ce_detail/<int:pk>/', core_views.CEDetailView.as_view(), name='ce_detail'),
            path('ce_create/', core_views.CECreateView.as_view(), name='ce_create'),
            path('ce_update/<int:pk>/', core_views.CEUpdateView.as_view(), name='ce_update'),
            path('ce_delete/<int:pk>/', core_views.CEDeleteView.as_view(), name='ce_delete'),
    #core END

    #prg_didactica BEGIN
        #Unidad
            path('unidad_list/', programacion_didactica_views.UDListView.as_view(), name='unidad_list'),
            path('unidad_detail/<int:pk>/', programacion_didactica_views.UDDetailView.as_view(), name='unidad_detail'),
            path('unidad_create/', programacion_didactica_views.UDCreateView.as_view(), name='unidad_create'),
            path('unidad_update/<int:pk>/', programacion_didactica_views.UDUpdateView.as_view(), name='unidad_update'),
            path('unidad_delete/<int:pk>/', programacion_didactica_views.UDDeleteView.as_view(), name='unidad_delete'),
        #InstEvaluacion
            path('ie_list/', programacion_didactica_views.InstEvListView.as_view(), name='ie_list'),
            path('ie_detail/<int:pk>/', programacion_didactica_views.InstEvDetailView.as_view(), name='ie_detail'),
            path('ie_create/', programacion_didactica_views.InstEvCreateView.as_view(), name='ie_create'),
            path('ie_update/<int:pk>/', programacion_didactica_views.InstEvUpdateView.as_view(), name='ie_update'),
            path('ie_delete/<int:pk>/', programacion_didactica_views.InstEvDeleteView.as_view(), name='ie_delete'),
        #PondRA
            path('pond_ra_list/', programacion_didactica_views.PondRAListView.as_view(), name='pond_ra_list'),
            path('pond_ra_detail/<int:pk>/', programacion_didactica_views.PondRADetailView.as_view(), name='pond_ra_detail'),
            path('pond_ra_create/', programacion_didactica_views.PondRACreateView.as_view(), name='pond_ra_create'),
            path('pond_ra_update/<int:pk>/', programacion_didactica_views.PondRAUpdateView.as_view(), name='pond_ra_update'),
            path('pond_ra_delete/<int:pk>/', programacion_didactica_views.PondRADeleteView.as_view(), name='pond_ra_delete'),
        #PondCriterio
            path('pond_ce_list/', programacion_didactica_views.PondCritListView.as_view(), name='pond_ce_list'),
            path('pond_ce_detail/<int:pk>/', programacion_didactica_views.PondCritDetailView.as_view(), name='pond_ce_detail'),
            path('pond_ce_create/', programacion_didactica_views.PondCritCreateView.as_view(), name='pond_ce_create'),
            path('pond_ce_update/<int:pk>/', programacion_didactica_views.PondCritUpdateView.as_view(), name='pond_ce_update'),
            path('pond_ce_delete/<int:pk>/', programacion_didactica_views.PondCritDeleteView.as_view(), name='pond_ce_delete'),
        #PondCritUD
            path('pond_ce_ud_list/', programacion_didactica_views.PondCritUDListView.as_view(), name='pond_ce_ud_list'),
            path('pond_ce_ud_detail/<int:pk>/', programacion_didactica_views.PondCritUDDetailView.as_view(), name='pond_ce_ud_detail'),
            path('pond_ce_ud_create/', programacion_didactica_views.PondCritUDCreateView.as_view(), name='pond_ce_ud_create'),
            path('pond_ce_ud_update/<int:pk>/', programacion_didactica_views.PondCritUDUpdateView.as_view(), name='pond_ce_ud_update'),
            path('pond_ce_ud_delete/<int:pk>/', programacion_didactica_views.PondCritUDDeleteView.as_view(), name='pond_ce_ud_delete'),
    #prg_didactica END
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
