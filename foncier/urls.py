from django.urls import path

from .import views

app_name = 'foncier'






urlpatterns = [
    path('DimFoncier/',views.DimFon,name='DimFoncier'),
    path('DimFoncierGouvernanc/',views.DFG,name='DimFoncierGouvernanc'),
    path('DimGeographie/',views.DG,name='DimGeographie'),
    path('FactFoncier/',views.FF,name='FactFoncier'),
    path('de_ffed<int:id>/',views.delete_ff,name='de_ffed'),
    path('up_ffe<int:id>/',views.update_ff,name='up_ffe'),
    path('de_fonc<int:id>/',views.delete_up_fonc,name='de_fonc'),
    path('up_fonc<int:id>/',views.update_fonc,name='up_fonc'),
    path('de_fon<int:id>/',views.delete_up_Gouve,name='de_fon'),
    path('up_fon<int:id>/',views.update_up_Gouve,name='up_fon'),
    path('up_geo<int:id>/',views.update_geo,name='up_geo'),
    path('de_geo<int:id>/',views.delete_geo,name='de_geo'),


]
