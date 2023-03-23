from django.db import models

# Create your models here.


class DimPecheArtisan(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ActPech_Artisan = models.CharField(max_length=250)
    NbrActeur = models.IntegerField()
    GroupPecheur = models.CharField(max_length=250)
    NbreGIEPecheur = models.IntegerField()
    NbrOrganiProfessPecheur = models.IntegerField()
    Nbr_AssociatPecheur = models.IntegerField()
    GroupMareyeur = models.CharField(max_length=250)
    NbreGIEMarey = models.IntegerField()
    NbrOrganiProfessMarey = models.IntegerField()
    Nbr_AssociatMarey = models.IntegerField()
    NbreQuaiPech = models.IntegerField()
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
    Qteannuel_debarq = models.IntegerField()
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
    
    date = models.DateTimeField()
    date_modification = models.DateTimeField()
    
    
    def __str__(self):
        return self.ActPech_Artisan


class DimPecheAssure(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)

    OffreAssureExistPech = models.CharField(max_length=25)
    TypeAssurancPech = models.CharField(max_length=25)
    NbreSouscripPech = models.IntegerField()
    NbrePrimePech = models.IntegerField()
    BesoinFormatPech = models.CharField(max_length=250)
    ActeurSensibilisePech = models.CharField(max_length=250)
    ActeurFormatPech = models.CharField(max_length=250)
    BesoinSensibilisePech = models.CharField(max_length=250)
    ContraintGlobPech = models.CharField(max_length=250)
    ContrainMajFilier = models.CharField(max_length=250)
    NbrInfrastruStokCondition=models.IntegerField()
    NbrFourniEmblag=models.IntegerField()
    NbrProdLabel=models.IntegerField()
    
    date = models.DateTimeField()
    date_modification = models.DateTimeField()


    def __str__(self):

        return self.nomCommune 


class DimPecheCommerce(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ProdVendType = models.DecimalField(max_digits=10, decimal_places=5)
    ProdVendCampgnInterSais = models.DecimalField(max_digits=10, decimal_places=5)
    ProdVendCampgnHiver = models.DecimalField(max_digits=10, decimal_places=5)
    ProdVendCampSaisFroid = models.DecimalField(max_digits=10, decimal_places=5)
    ProdVendCampPrintem = models.DecimalField(max_digits=10, decimal_places=5)
    Type_VentPech = models.CharField(max_length=250)
    PriVentMoy_Prod= models.IntegerField()
    Mod_ecoulement = models.CharField(max_length=250)
    ClientPech = models.CharField(max_length=250)
    date= models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.nomCommune)


class DimPecheFinance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffrServicFinancPech = models.CharField(max_length=25)
    DemandApportPech = models.CharField(max_length=25)
    TypGaranExige = models.CharField(max_length=250)
    LongProcedCredi = models.CharField(max_length=250)
    TauInteret = models.CharField(max_length=250)
    DelaiRemboursMinMax = models.CharField(max_length=250)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()
  

    def __str__(self):
        return self.OffrServicFinancPech


class DimPecheInnovat(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    TechnoIntrod = models.CharField(max_length=250)
    TechnoAdopte = models.CharField(max_length=25)
    CausNoAdoption = models.CharField(max_length=250)
    CausTechnoNoAdop = models.CharField(max_length=250)
    date= models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return self.TechnoIntrod


class DimPecheTAInnovat(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    TechnoIntroTA = models.CharField(max_length=250)
    TechnoAdoptTA = models.CharField(max_length=25)
    CausNoAdoptTA = models.CharField(max_length=250)
    CausTechnoNoAdopTA = models.CharField(max_length=250)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return self.TechnoIntroTA


class DimPechTAAssurance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffreAssurTA = models.CharField(max_length=250)
    TypAssurTA = models.CharField(max_length=250)
    NbrSouscripTA =models.CharField(max_length=250)
    NivPrimTA = models.CharField(max_length=250)
    BesoinformTA = models.CharField(max_length=250)
    ContraintGlobTA = models.CharField(max_length=250)
    ContrainMajFilierTA = models.CharField(max_length=250)
  
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):

        return self.OffreAssurTA


class DimPechTACommerc(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ProdVenduCampagTA = models.CharField(max_length=300)
    TypVentTA = models.CharField(max_length=300)
    PrixVentMoyProdTA = models.DecimalField(max_digits=10, decimal_places=5)
    
    ModEcoulmtTA = models.CharField(max_length=300)
    ClientTA = models.CharField(max_length=300)
    datet = models.DateTimeField()
    date_modification = models.DateTimeField()
    
    def __str__(self):

        return self.ProdVenduCampagTA


class DimPechTAFinance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffrServicFinancTA = models.CharField(max_length=25)
    DemandApportTA = models.CharField(max_length=25)
    TypGaranExigeTA = models.CharField(max_length=250)
    LongProcedCrditTA = models.CharField(max_length=250)
    MontanMoyTA = models.DecimalField(max_digits=10, decimal_places=5)
    TauInterTA = models.CharField(max_length=250)
    DelaiRemboursMinMaxTA = models.CharField(max_length=250)
  
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return self.OffrServicFinancTA


class DimPechTransformArtisan(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ActTransfArtisan = models.CharField(max_length=25)
    GrptTransformtrTA = models.CharField(max_length=25)
    TypServicOffrGIE = models.CharField(max_length=250)
    TypServicOffrAssocia = models.CharField(max_length=250)
    TypServicOffrOrgProf = models.CharField(max_length=250)
    FourniIntranMatTrans= models.CharField(max_length=250)
    SitTransform= models.CharField(max_length=250)
    MatEquipTransExist = models.CharField(max_length=250)
    
    TypProdTransfPeriod = models.CharField(max_length=250)
    SourcApproIntranMatTA = models.CharField(max_length=250)
    QteProdPeriodTA = models.DecimalField(max_digits=10, decimal_places=5)
    QteProdTypeTA = models.DecimalField(max_digits=10, decimal_places=5)
    TauxTransformArtisan = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return self.TauxTransformArtisan




class Visiteur (models.Model):
    nom = models.CharField(max_length=25)
    date_visiteur = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom

    