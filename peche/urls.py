
from django.urls import path

from peche import views


app_name = 'peche'


urlpatterns = [
    path('dimpecart/', views.pec_art, name='dimpecart'),
    path('dimpecass/', views.pech_assu, name='dimpecass'),
    path('dimpecec/', views.pech_ec, name='dimpecec'),
    path('dimpecfin/', views.pech_fin, name='dimpecfin'),
    path('up_ar<int:id>/', views.update_ar, name='up_ar'),
    path('de_ar<int:id>/', views.delete_ar, name='de_ar'),
    path('up_ass<int:id>/', views.update_ass, name='up_ass'),
    path('de_ass<int:id>/', views.delete_ass, name='de_ass'),
    path('up_fin<int:id>/', views.update_fin, name='up_fin'),
    path('de_fin<int:id>/', views.delete_fin, name='de_fin'),
    path('up_com<int:id>/', views.update_com, name='up_com'),
    path('de_com<int:id>/', views.delete_com, name='de_com'),
    # ath('dimagroog/',views.dimagroorg_form,name='dimagroorg'),
    path('pech_ino/', views.pech_inov, name='pech_ino'),
    path('up_ino<int:id>/', views.update_ino, name='up_ino'),
    path('de_ino<int:id>/', views.delete_ino, name='de_ino'),
    path('pech_trans/', views.pechtrans, name='pech_trans'),
    path('update_trs<int:id>/', views.update_trs, name='update_trs'),
    path('delete_trs<int:id>/', views.delete_trs, name='delete_trs'),
    path('pech_taassu/', views.pechtassu, name='pech_taassu'),
    path('up_tassu<int:id>/', views.update_tassu, name='up_tassu'),
    path('de_tassu<int:id>/', views.delete_tasuu, name='de_tassu'),
    path('pech_tacom/', views.petacom, name='pech_tacom'),
    path('up_tc<int:id>/', views.update_tacom, name='up_tc'),
    path('de_tc<int:id>/', views.delete_tacom, name='de_tc'),
    path('pech_taino/', views.pech_tainov, name='pech_taino'),
    path('up_taino<int:id>/', views.up_taino, name='up_taino'),
    path('de_taino<int:id>/', views.de_taino, name='de_taino'),
    path('pech_tafina/', views.pechtafina, name='pech_tafina'),
    path('up_fi<int:id>/', views.up_fina, name='up_fi'),
    path('de_fi<int:id>/', views.de_fina, name='de_fi'),
    path('pech_fac/', views.pechfac, name='pech_fac'),
    path('up_fat<int:id>/', views.up_fac, name='up_fat'),
    path('de_fat<int:id>/', views.de_fac, name='de_fat'),

]
