from django.forms import ModelForm
from education.models import DimEduc_Access
from django import forms


class acc(ModelForm):

    CodeCommune = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    CodeTemps = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEnsembleGarconsEntre3et5ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEnsembleFillesEntre3et5ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEnsembleFillesEtGarconsAgeEntre3Et5ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifGarconsInscritsPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifFilleInscritPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifTotalInscritPrescolaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifPrescolairePetiteSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffcetifPresccolaireMoyenSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifPrescolaireGrandeSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffcetifPresccolaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreGarconsFillesEnPetiteSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreGarconsFillesEnMoyenneSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreGarconsFillesEnGrandeSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreFillesPrescolaireTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifTotalInscritPrescolairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectitTotalElevesInscritsPrescolaireStructureCommunautaires = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifTotalElevesInscritPrecolairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifTotalElevesFillesInscritPrecolairePrive = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifTotalElevesFillesIncritDansLesStructureCommunautaires = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifTotalElevesFillesInscritsAuPrescolaireStructureCommunautaire = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreTotalNouveauxInscritsPetiteSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreTotalNouveauxInscritsMoyenneSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreTotalNouveauxInscritGrandeSection = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreStructurePrescolairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreStructurePrescolairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreStructurePrescolaireCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifElevesPrescolaireAyantPieceEtatCivilPetiteSection = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifElevesPrescolaireAyantPieceEtatCivilMoyenneSection = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifPrecolaireAyantPieceEtatCivilGrandeSection = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoEffectifEnfantsPrescolaireFrancoArabe = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreDaaraModerne = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessPrescoNombreDaaraMiseAJour = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreGarconsDe6A11ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreFillesDe6A11ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessElNombreEnfantsDe6A11ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreEleveElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreGarconsElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreFillesElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElementairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElementairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElementaireStructuresCommunautaires = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElevesElementaireSituationHandicap = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsFillesElementaireSituationHandicap = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifGarconsElementaireSituationHandicap = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifTotalElevesElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifTotalElevesPasPieceEtatCivil = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifTotalElevesCI = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectilTotalElevesCM2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsEnfantsElementaireFrancoArabe = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElementaireRedoublantsTotal = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElementaireRedoublantsFilles = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsElementaireRedoublantGarcons = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsCI = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsCP = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsCE1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsCE2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsCM1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifsCM2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreRedoublantCI = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreRedoublantCP = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreRedoublantsCE1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreRedoublantsCE2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreRedoublantsCM1 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreRedoublantsCM2 = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifTotalInscritElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifGarconsInscritsElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElEffectifFillesIncritesElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreElevesSituationHandicap = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreTotalElevesElementaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElPopulationOfficiellementScolarisableJeunes6_11ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElPopulationOfficiellementScolarisableGarcons6_11ans = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElPopulationOfficiellementScolarisableFilles6_11ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreElevesQuittantEtablissementPourHorsCommune = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreElevesProvenanceEtablissementSeSituantDansUneAutreCommune = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreEcoleElementairePubliques = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessElNombreEcolesElementairePrivees = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEnsembleGarconsEntre12Et15ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEnsembleFillesEntre12Et15ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesFilles = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesGarcons = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifsMoyenGeneralPublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifMoyenGeneralPrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGRedoublantsTotalMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGRedoublantsFillesMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGRedoublantsGarconsMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifsInscritMoyenGeneralFrancoArabe = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifsMoyenGeneral6eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifsMoyenGeneral5eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifMoyenGeneral4e = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifMoyenGeneral3e = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreRedoublants6e = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreRedoublants5e = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreRedoublants4e = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreRedoublants3e = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGEffectifTotalIncritMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGPopulationJeunesTranche12_15ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesEffectivementInscrit6eme1erFois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreNouveauxInscritFilles6eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreTotalNouveauxInscrit6eme = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreNouveauxInscrits6emePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesSituationHandicapMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreTotalElevesMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesMarieeCoursAnneeMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreElevesFillesVictimesGrossesseMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreFillesVictimesViolencesSexuellesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombresGarconsVictimesViolencesSexuellesMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreFillesOrphelinsMG = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreTotalFilleMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AccessMGNombreGarconsOrphelinsMoyenGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeGarconsAge16_18ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeFillesAgee16_18ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEnsFillesGarconsAgee16_18ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreEleveSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreGarconsSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreFillesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifsSecondairePublic = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifsSecondairePrive = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifsSecondaireCommunautaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeRedoublantsTotalSecondaireGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeRedoublantsFillesSecondaireGeneral = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeRedoublantsGarconsSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifs2nd = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifs1er = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifsTerminale = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreRedoublants2nd = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreRedoublants1er = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreRedoublantsTerminale = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeEffectifTotalInscritSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSePopulationJeunesTranche16_18ans = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreElevesSituationHandicapSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreTotalElevesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreFillesMarieeEnCoursAnneeSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreElevesFillesVictimesGrossesseSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreElevesVictimesViolencesSexuellesEtablissement = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombresFillesVictimesViolencesSexuellesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreGarconsVictimesViolencesSexuellesSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreElevesOrphelinsSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreFillesOrphelinsSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreGarconsOrphelinsSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    AcessSeNombreElevesSansPieceEtatCivilSecondaire = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Access
        fields = "__all__"
