from django.db import models

# Create your models here.


class DimPecheArtisan(models.Model):
    ActPech_Artisan = models.CharField(max_length=250)
    GroupPecheur = models.CharField(max_length=250)
    GroupMareyeur = models.CharField(max_length=250)
    TypePirogu = models.CharField(max_length=250)
    TypProdPechPirogBois = models.CharField(max_length=250)
    TypProdPechPirogFibr = models.CharField(max_length=250)
    TypProdPechPirogAlumin = models.CharField(max_length=250)
    TypeProdHalieuHiver = models.CharField(max_length=250)
    TypeProdHalieuInterSaison = models.CharField(max_length=250)
    TypeProdHalieuSaisFroid = models.CharField(max_length=250)
    TypeProdHalieuPrimptem = models.CharField(max_length=250)
    IntrantPech = models.CharField(max_length=250)
    MatUtilisePech = models.CharField(max_length=250)
    SourcApprovis_Intran = models.CharField(max_length=250)
    SourcApprovis_Materiel = models.CharField(max_length=250)
    NivCaptMoyenHiver = models.CharField(max_length=250)
    NivCaptMoyenInterSaison = models.CharField(max_length=250)
    NivCaptMoyenSaisFroid = models.CharField(max_length=250)
    NivCaptMoyenPrintem = models.CharField(max_length=250)
    NivCaptMoyenSortTypProd = models.CharField(max_length=250)
    NivPertPostCaptHiver = models.CharField(max_length=250)
    NivPertPostCaptInterSaison = models.CharField(max_length=250)
    NivPertPostCaptSaisFroid = models.CharField(max_length=250)
    NivPertPostCaptPrintem = models.CharField(max_length=250)
    NivPertPostCaptTypProd = models.CharField(max_length=250)
    # date =models.DateTimeField()

    def __str__(self):
        return self.ActPech_Artisan


class DimPecheAssure(models.Model):
    TypeAssurancPech = models.CharField(max_length=25)
    OffreAssureExistPech = models.CharField(max_length=25)
    BesoinFormatPech = models.CharField(max_length=250)
    ActeurSensibilisePech = models.CharField(max_length=250)
    ActeurFormatPech = models.CharField(max_length=250)
    BesoinSensibilisePech = models.CharField(max_length=250)
    ContraintGlobPech = models.CharField(max_length=250)
    ContrainMajFilier = models.CharField(max_length=250)
    # date = models.DateTimeField()

    def __str__(self):

        return self.TypeAssurancPech


class DimPecheCommerce(models.Model):
    ProdVendType = models.IntegerField()
    ProdVendCampgnInterSais = models.IntegerField()
    ProdVendCampgnHiver = models.IntegerField()
    ProdVendCampSaisFroid = models.IntegerField()
    ProdVendCampPrintem = models.IntegerField()
    Type_VentPech = models.CharField(max_length=250)
    Mod_ecoulement = models.CharField(max_length=250)
    ClientPech = models.CharField(max_length=250)

    def __str__(self):
        return str(self.ProdVendType)


class DimPecheFinance(models.Model):
    OffrServicFinancPech = models.CharField(max_length=25)
    DemandApportPech = models.CharField(max_length=25)
    TypGaranExige = models.CharField(max_length=250)
    LongProcedCredi = models.CharField(max_length=250)
    DemandApportPech = models.CharField(max_length=25)
    TauInteret = models.CharField(max_length=250)
    DelaiRemboursMinMax = models.CharField(max_length=250)
    # date = models.DateTimeField()

    def __str__(self):
        return self.OffrServicFinancPech


class DimPecheInnovat(models.Model):
    TechnoIntrod = models.CharField(max_length=250)
    TechnoAdopte = models.CharField(max_length=25)
    CausNoAdoption = models.CharField(max_length=250)
    CausTechnoNoAdop = models.CharField(max_length=250)

    def __str__(self):
        return self.TechnoIntrod


class DimPecheTAInnovat(models.Model):
    TechnoIntroTA = models.CharField(max_length=250)
    TechnoAdoptTA = models.CharField(max_length=25)
    CausNoAdoptTA = models.CharField(max_length=250)
    CausTechnoNoAdop = models.CharField(max_length=250)

    def __str__(self):
        return self.TechnoIntroTA


class DimPechTAAssurance(models.Model):
    OffreAssurTA = models.CharField(max_length=250)
    TypAssurTA = models.CharField(max_length=250)
    NivPrimTA = models.CharField(max_length=250)
    BesoinformTA = models.CharField(max_length=250)
    ContraintGlobTA = models.CharField(max_length=250)
    ContrainMajFilierTA = models.CharField(max_length=250)
    # date = models.DateTimeField()

    def __str__(self):

        return self.OffreAssurTA


class DimPechTACommerc(models.Model):
    ProdVenduCampagTA = models.IntegerField()
    TypVentTA = models.IntegerField()
    ModEcoulmtTA = models.IntegerField()
    ClientTA = models.IntegerField()

    def __str__(self):

        return self.ProdVenduCampagTA


class DimPechTAFinance(models.Model):
    OffrServicFinancTA = models.CharField(max_length=25)
    DemandApportTA = models.CharField(max_length=25)
    TypGaranExigeTA = models.CharField(max_length=250)
    LongProcedCrditTA = models.CharField(max_length=250)
    TauInterTA = models.CharField(max_length=250)
    DelaiRemboursMinMaxTA = models.CharField(max_length=250)
    # date =models.DateTimeField()

    def __str__(self):
        return self.OffrServicFinancTA


class DimPechTransformArtisan(models.Model):
    ActTransfArtisan = models.CharField(max_length=25)
    GrptTransformtrTA = models.CharField(max_length=25)
    TypServicOffrGIE = models.CharField(max_length=250)
    TypServicOffrAssocia = models.CharField(max_length=250)
    TypServicOffrOrgProf = models.CharField(max_length=250)
    MatEquipTransExist = models.CharField(max_length=250)
    TypProdTransfPeriod = models.CharField(max_length=250)
    SourcApproIntranMatTA = models.CharField(max_length=250)
    QteProdPeriodTA = models.IntegerField()
    QteProdTypeTA = models.IntegerField()
    TauxTransformArtisan = models.IntegerField()

    def __str__(self):
        return self.TauxTransformArtisan


class FactPeche(models.Model):

    IdPechArtisan = models.ForeignKey(
        DimPecheArtisan, on_delete=models.CASCADE)
    IdPechAssure = models.ForeignKey(DimPecheAssure, on_delete=models.CASCADE)
    IdPechComm = models.ForeignKey(DimPecheCommerce, on_delete=models.CASCADE)
    IdPechFinance = models.ForeignKey(
        DimPecheFinance, on_delete=models.CASCADE)
    IdPechInnov = models.ForeignKey(DimPecheInnovat, on_delete=models.CASCADE)
    IdPechInnovTA = models.ForeignKey(
        DimPecheTAInnovat, on_delete=models.CASCADE)
    IdPechTAAssure = models.ForeignKey(
        DimPechTAAssurance, on_delete=models.CASCADE)
    IdPechTAComm = models.ForeignKey(
        DimPechTACommerc, on_delete=models.CASCADE)
    IdPechTAFinance = models.ForeignKey(
        DimPechTAFinance, on_delete=models.CASCADE)
    IdPechTransFormArtisan = models.ForeignKey(
        DimPechTransformArtisan, on_delete=models.CASCADE)
    IdPechAssure = models.ForeignKey(DimPecheAssure, on_delete=models.CASCADE)
    IdPechComm = models.ForeignKey(DimPecheCommerce, on_delete=models.CASCADE)
    IdPechArtisan = models.ForeignKey(
        DimPecheArtisan, on_delete=models.CASCADE)
    IdPechAssure = models.ForeignKey(DimPecheAssure, on_delete=models.CASCADE)
    IdPechComm = models.ForeignKey(DimPecheCommerce, on_delete=models.CASCADE)
    QteProdPeriodTA = models.IntegerField()
    QteProdTypeTA = models.IntegerField()
    TauxTransformArtisan = models.IntegerField()
    IdGeographie = models.IntegerField()
    NbrActeur = models.IntegerField()
    NbreGIEPecheur = models.IntegerField()
    NbrOrganiProfessPecheur = models.IntegerField()
    Nbr_AssociatPecheur = models.IntegerField()
    NbrOrganiProfessMarey = models.IntegerField()
    Nbr_AssociatMarey = models.IntegerField()
    NbreQuaiPech = models.IntegerField()
    NbrPirogBois = models.IntegerField()
    NbrePirogFibVer = models.IntegerField()
    NbrPirogAlumin = models.IntegerField()
    NbrePirogImmatri = models.IntegerField()
    NbreSouscripPech = models.IntegerField()
    NbrePrimePech = models.IntegerField()
    Qteannuel_debarq = models.IntegerField()
    NbrSouscripTA = models.IntegerField()
    QteProdTypeTA = models.IntegerField()
    PrixVentMoyProdTA = models.IntegerField()

    def __str__(self):
        return self.IdPechArtisan
