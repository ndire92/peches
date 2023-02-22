
from django.urls import path

from sante import views


app_name = 'sante'


urlpatterns = [
    path('PlanificationFamiliale/', views.pltfm, name='PlanificationFamiliale'),
    path('updatepl/<int:id>/', views.update_P, name='updatepl'),
    path('deletepl/<int:id>/', views.delete_P, name='deletepl'),
    path('ReproductionEtJeune/', views.repjeu, name='ReproductionEtJeune'),
    path('up_repro/<int:id>/', views.update_repro, name='up_repro'),
    path('de_repro/<int:id>/', views.delete_repro, name='de_repro'),
    # path('SanteAlimentationEtNutrition/', views.san,
    #     name='SanteAlimentationEtNutrition'),
    # path('up_san/<int:id>/', views.update_ali, name='up_san'),
    # path('de_sanl/<int:id>/', views.delete_ali, name='de_san'),
    path('SantePaludisme/', views.spld, name='SantePaludisme'),
    path('up_palu/<int:id>/', views.update_palu, name='up_palu'),
    path('de_palu/<int:id>/', views.delete_palu, name='de_palu'),
    path('survienfant/', views.survie, name='survienfant'),
    path('up_vie/<int:id>/', views.update_vie, name='up_vie'),
    path('de_vie/<int:id>/', views.delete_vie, name='de_vie'),
    # path('gouvsante/', views.gouvsante, name='gouvsante'),
    # path('up_gsante/<int:id>/', views.update_gouvsnt, name='up_gsante'),
    # path('de_gsante/<int:id>/', views.delete_gouvsnt, name='de_gsante'),
    path('vacination/', views.vaci, name='vacination'),
    path('up_vac/<int:id>/', views.update_vaci, name='up_vac'),
    path('de_vac/<int:id>/', views.delete_vaci, name='de_vac'),


]
