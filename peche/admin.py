from django.contrib import admin

from peche.models import DimPecheArtisan,DimPechTransformArtisan,DimPechTAFinance,DimPechTACommerc, DimPechTAAssurance,DimPecheTAInnovat,DimPecheInnovat,DimPecheAssure,DimPecheCommerce,DimPecheFinance

# Register your models here.
admin.site.register(DimPecheArtisan)
admin.site.register(DimPecheAssure)
admin.site.register(DimPecheCommerce)
admin.site.register(DimPecheFinance)

admin.site.register(DimPecheInnovat)
admin.site.register(DimPecheTAInnovat)
admin.site.register( DimPechTAAssurance)
admin.site.register(DimPechTACommerc)

admin.site.register(DimPechTAFinance)
admin.site.register(DimPechTransformArtisan)

