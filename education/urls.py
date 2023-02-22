from django.urls import path

from .import views

app_name = 'education'


urlpatterns = [
    path('DimEqui/', views.DimEq, name='DimEqui'),
    path('DimGou/', views.DG, name='DimGou'),
    path('DimPer/', views.DP, name='DimPer'),
    path('Dimp/', views.person, name='Dimp'),
    path('dim_Access/', views.dis, name='dim_Access'),
    path('up_acc/<int:id>/', views.update_acc, name='up_acc'),
    path('de_acc/<int:id>/', views.delete_acc, name='de_acc'),
    path('update_equ/<int:id>/', views.update_eq, name='update_equ'),
    path('delete_eq/<int:id>/', views.delete_eq, name='delete_eq'),
    path('update_dg/<int:id>/', views.update_gv, name='update_dg'),
    path('delete_dg/<int:id>/', views.delete_gv, name='delete_dg'),
    path('update_per/<int:id>/', views.update_perso, name='update_per'),
    path('delete_per/<int:id>/', views.delete_perso, name='delete_per'),
    path('update_perf/<int:id>/', views.update_perfor, name='update_perf'),
    path('delete_perf/<int:id>/', views.delete_perfor, name='delete_perf'),
    # path('dimagroprod/',views.dimagrprod_form,name='dimagroprod'),
    # path('dimagrovcul/',views.dimagrovcul_form,name='dimagrovcul'),

]
