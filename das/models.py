from django.db import models


# Create your models here.
class DimAgroAssurance(models.Model):

    OffreuAssurance = models.CharField(max_length=300)
    TypeAssurance = models.CharField(max_length=300)
    CulturAssure = models.CharField(max_length=300)
    NivPrime = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)


class DimAgroCommercial(models.Model):

    ProdVenteSpecul = models.CharField(max_length=300)
    TypeVente = models.CharField(max_length=300)
    MarchRegroupement = models.CharField(max_length=300)
    ClientAgro = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ProdVenteSpecul


class DimAgroCulture (models.Model):

    ZonProd_Cult = models.CharField(max_length=300)
    Cultur_Pratique = models.CharField(max_length=300)
    Type_Semence = models.CharField(max_length=300)
    Type_Culture_Pratique = models.CharField(max_length=250)
    VarieteCultive = models.CharField(max_length=250)
    SourcApprovisIntran = models.CharField(max_length=300)
    SourcApprovisSemenc = models.CharField(max_length=300)
    SourcApprovisEngrProdPhyto = models.CharField(max_length=300)
    SourcApprovisMatAgro = models.CharField(max_length=300)
    TypeAcquisIntran = models.CharField(max_length=300)
    TypeAcquisMat = models.CharField(max_length=300)
    TypeFertilisUtil = models.CharField(max_length=300)
    TypePesticidUtil = models.CharField(max_length=300)
    ModAcquisParcel = models.CharField(max_length=300)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.ZonProd_Cult


class DimAgroFinance(models.Model):

    OffreServicFinance = models.CharField(max_length=300)
    DemandApport = models.CharField(max_length=250)
    TypeGaranExige = models.CharField(max_length=300)
    LongProcedCredi = models.IntegerField()
    DelaiRembourse = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.OffreServicFinance


class DimAgroOrganisation(models.Model):
    name_Organisation = models.CharField(max_length=300)
    TypeServicOfferOP = models.CharField(max_length=300)
    BesoinForm = models.CharField(max_length=300)
    ContrainGlobalAgro = models.CharField(max_length=300)
    ContrainMajFilier = models.CharField(max_length=300)
    InfrasStockCondition = models.CharField(max_length=300)
    FournisEmballag = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_Organisation


class DimAgroProduction(models.Model):

    name_Production = models.CharField(max_length=300)
    CodeCulture = models.IntegerField()
    type_cult_prat = models.CharField(max_length=250)
    RendemHectarCult = models.IntegerField()
    TauxPertPostRecoltParCult = models.IntegerField()
    TypeSolExist = models.CharField(max_length=300)
    TypeDegradZonCultur = models.CharField(max_length=300)
    CauseDegrad = models.CharField(max_length=300)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_Production


class FactAgriculture(models.Model):
    IdProduction_FK = models.ForeignKey(
        DimAgroProduction, on_delete=models.CASCADE)
    # Field name made lowercase.
    idorganisation_fk = models.ForeignKey(
        DimAgroOrganisation, on_delete=models.CASCADE)
    # Field name made lowercase.
    idagrofinance_fk = models.ForeignKey(
        DimAgroFinance, on_delete=models.CASCADE)
    # Field name made lowercase.
    idculture_fk = models.ForeignKey(DimAgroCulture, on_delete=models.CASCADE)
    # Field name made lowercase.
    numagrocommercial_fk = models.ForeignKey(
        DimAgroCommercial, on_delete=models.CASCADE)
    # Field name made lowercase.
    idagroassurance_fk = models.ForeignKey(
        DimAgroAssurance, on_delete=models.CASCADE)
    ZonProd_Cult = models.CharField(max_length=300)
    SupMoyDetenuMenag = models.IntegerField()
    NbrSouscript = models.IntegerField()
    PrixVentMoySaison = models.IntegerField()
    MontMoyTypeCultur = models.IntegerField()

    TauxInteret = models.IntegerField()
    SupMaxDetenu = models.IntegerField()
    SupMinDetenu = models.IntegerField()
    SupMoyDetenu = models.IntegerField()
    SupMoyEmblave = models.IntegerField()
    RendemHectarCult = models.IntegerField()
    TauxPertPostRecoltParCult = models.IntegerField()

    def __str__(self):
        return str(self.date)

    def __str__(self):
        return self.OffreuAssurance


class MultiStepFormModel(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    gplus = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = models.Manager()
