# Generated by Django 4.1.6 on 2023-04-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimPecheArtisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('ActPech_Artisan', models.CharField(max_length=250)),
                ('NbrActeur', models.IntegerField()),
                ('GroupPecheur', models.CharField(max_length=250)),
                ('NbreGIEPecheur', models.IntegerField()),
                ('NbrOrganiProfessPecheur', models.IntegerField()),
                ('Nbr_AssociatPecheur', models.IntegerField()),
                ('GroupMareyeur', models.CharField(max_length=250)),
                ('NbreGIEMarey', models.IntegerField()),
                ('NbrOrganiProfessMarey', models.IntegerField()),
                ('Nbr_AssociatMarey', models.IntegerField()),
                ('NbreQuaiPech', models.IntegerField()),
                ('TypePirogu', models.CharField(max_length=250)),
                ('TypProdPechPirogBois', models.CharField(max_length=250)),
                ('TypProdPechPirogFibr', models.CharField(max_length=250)),
                ('TypProdPechPirogAlumin', models.CharField(max_length=250)),
                ('TypeProdHalieuHiver', models.CharField(max_length=250)),
                ('TypeProdHalieuInterSaison', models.CharField(max_length=250)),
                ('TypeProdHalieuSaisFroid', models.CharField(max_length=250)),
                ('TypeProdHalieuPrimptem', models.CharField(max_length=250)),
                ('IntrantPech', models.CharField(max_length=250)),
                ('MatUtilisePech', models.CharField(max_length=250)),
                ('SourcApprovis_Intran', models.CharField(max_length=250)),
                ('SourcApprovis_Materiel', models.CharField(max_length=250)),
                ('Qteannuel_debarq', models.IntegerField()),
                ('NivCaptMoyenHiver', models.CharField(max_length=250)),
                ('NivCaptMoyenInterSaison', models.CharField(max_length=250)),
                ('NivCaptMoyenSaisFroid', models.CharField(max_length=250)),
                ('NivCaptMoyenPrintem', models.CharField(max_length=250)),
                ('NivCaptMoyenSortTypProd', models.CharField(max_length=250)),
                ('NivPertPostCaptHiver', models.CharField(max_length=250)),
                ('NivPertPostCaptInterSaison', models.CharField(max_length=250)),
                ('NivPertPostCaptSaisFroid', models.CharField(max_length=250)),
                ('NivPertPostCaptPrintem', models.CharField(max_length=250)),
                ('NivPertPostCaptTypProd', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheAssure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('OffreAssureExistPech', models.CharField(max_length=25)),
                ('TypeAssurancPech', models.CharField(max_length=25)),
                ('NbreSouscripPech', models.IntegerField()),
                ('NbrePrimePech', models.IntegerField()),
                ('BesoinFormatPech', models.CharField(max_length=250)),
                ('ActeurSensibilisePech', models.CharField(max_length=250)),
                ('ActeurFormatPech', models.CharField(max_length=250)),
                ('BesoinSensibilisePech', models.CharField(max_length=250)),
                ('ContraintGlobPech', models.CharField(max_length=250)),
                ('ContrainMajFilier', models.CharField(max_length=250)),
                ('NbrInfrastruStokCondition', models.IntegerField()),
                ('NbrFourniEmblag', models.IntegerField()),
                ('NbrProdLabel', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheCommerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('ProdVendType', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ProdVendCampgnInterSais', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ProdVendCampgnHiver', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ProdVendCampSaisFroid', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ProdVendCampPrintem', models.DecimalField(decimal_places=5, max_digits=10)),
                ('Type_VentPech', models.CharField(max_length=250)),
                ('PriVentMoy_Prod', models.IntegerField()),
                ('Mod_ecoulement', models.CharField(max_length=250)),
                ('ClientPech', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('OffrServicFinancPech', models.CharField(max_length=25)),
                ('DemandApportPech', models.CharField(max_length=25)),
                ('TypGaranExige', models.CharField(max_length=250)),
                ('LongProcedCredi', models.CharField(max_length=250)),
                ('TauInteret', models.CharField(max_length=250)),
                ('DelaiRemboursMinMax', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheInnovat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('TechnoIntrod', models.CharField(max_length=250)),
                ('TechnoAdopte', models.CharField(max_length=25)),
                ('CausNoAdoption', models.CharField(max_length=250)),
                ('CausTechnoNoAdop', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheTAInnovat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('TechnoIntroTA', models.CharField(max_length=250)),
                ('TechnoAdoptTA', models.CharField(max_length=25)),
                ('CausNoAdoptTA', models.CharField(max_length=250)),
                ('CausTechnoNoAdopTA', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTAAssurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('OffreAssurTA', models.CharField(max_length=250)),
                ('TypAssurTA', models.CharField(max_length=250)),
                ('NbrSouscripTA', models.CharField(max_length=250)),
                ('NivPrimTA', models.CharField(max_length=250)),
                ('BesoinformTA', models.CharField(max_length=250)),
                ('ContraintGlobTA', models.CharField(max_length=250)),
                ('ContrainMajFilierTA', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTACommerc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('ProdVenduCampagTA', models.CharField(max_length=300)),
                ('TypVentTA', models.CharField(max_length=300)),
                ('PrixVentMoyProdTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('ModEcoulmtTA', models.CharField(max_length=300)),
                ('ClientTA', models.CharField(max_length=300)),
                ('datet', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTAFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('OffrServicFinancTA', models.CharField(max_length=25)),
                ('DemandApportTA', models.CharField(max_length=25)),
                ('TypGaranExigeTA', models.CharField(max_length=250)),
                ('LongProcedCrditTA', models.CharField(max_length=250)),
                ('MontanMoyTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TauInterTA', models.CharField(max_length=250)),
                ('DelaiRemboursMinMaxTA', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTransformArtisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeCommune', models.IntegerField()),
                ('nomCommune', models.CharField(max_length=300)),
                ('ActTransfArtisan', models.CharField(max_length=25)),
                ('GrptTransformtrTA', models.CharField(max_length=25)),
                ('TypServicOffrGIE', models.CharField(max_length=250)),
                ('TypServicOffrAssocia', models.CharField(max_length=250)),
                ('TypServicOffrOrgProf', models.CharField(max_length=250)),
                ('FourniIntranMatTrans', models.CharField(max_length=250)),
                ('SitTransform', models.CharField(max_length=250)),
                ('MatEquipTransExist', models.CharField(max_length=250)),
                ('TypProdTransfPeriod', models.CharField(max_length=250)),
                ('SourcApproIntranMatTA', models.CharField(max_length=250)),
                ('QteProdPeriodTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('QteProdTypeTA', models.DecimalField(decimal_places=5, max_digits=10)),
                ('TauxTransformArtisan', models.DecimalField(decimal_places=5, max_digits=10)),
                ('date', models.DateTimeField()),
                ('date_modification', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Visiteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('date_visiteur', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
