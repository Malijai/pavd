from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Typepub(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    reponse = models.CharField(max_length=200, )

    def __str__(self):
        return '%s' % self.reponse


class Typestud(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    reponse = models.CharField(max_length=200, )

    def __str__(self):
        return '%s' % self.reponse

class Quanti(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    reponse = models.CharField(max_length=200, )
    catego = models.IntegerField()

    def __str__(self):
        return '%s' % self.reponse


class Quali(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    reponse = models.CharField(max_length=200, )

    def __str__(self):
        return '%s' % self.reponse


class Articles(models.Model):
    docid = models.IntegerField(blank=True, null=True, verbose_name="1- Document ID",)
    title = models.CharField(max_length=250, verbose_name="2- Titre de la publication")
    authors = models.CharField(max_length=250, verbose_name="3- Auteurs séparés par un ;")
    year = models.IntegerField(verbose_name="4- Année de la publication",)
    type = models.ForeignKey(Typepub, null=True,blank=True, on_delete=models.DO_NOTHING, verbose_name="5- Type de publication")
    othertype = models.CharField(blank=True, null=True, max_length=250, verbose_name="5a- Si autre type de publication")
    peer = models.BooleanField(default=False, verbose_name="6- Peer reviewed (cocher si oui)?")
    meeting = models.BooleanField(default=False, verbose_name="7a- Data source: Meetings with participants?")
    record = models.BooleanField(default=False, verbose_name="7b- Data source: Records?")
    psychotest = models.BooleanField(default=False, verbose_name="7c- Data source: Presence of psychometric tests?")
    otherdata = models.CharField(blank=True, null=True, max_length=250, verbose_name="7c1- List of psychometric tests")
    studytype = models.ForeignKey(Typestud, on_delete=models.DO_NOTHING, verbose_name="8- Study type")
    designquanti1 = models.ForeignKey(Quanti, null=True,blank=True, related_name='quanti1', on_delete=models.DO_NOTHING, verbose_name="9a- Study design (if qualitative)")
    designquanti2 = models.ForeignKey(Quanti, null=True,blank=True, related_name='quanti2', on_delete=models.DO_NOTHING, verbose_name="9b- Study design (if qualitative)")
    designquali = models.ForeignKey(Quali, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name="10- Study design (if qualitative)")
    otherqual = models.CharField(blank=True, null=True, max_length=100, verbose_name="10a- If other specify")
    nparticipant = models.CharField(blank=True, null=True, max_length=250, verbose_name="11- Number of participants")
    ratiomf = models.CharField(blank=True, null=True, max_length=250, verbose_name="12- Males / Females")
    age = models.CharField(blank=True, null=True, max_length=250, verbose_name="13- Ages")
    ethno = models.CharField(blank=True, null=True, max_length=250, verbose_name="14- Ethno-racial group")
    education = models.CharField(blank=True, null=True, max_length=250, verbose_name="15- Education")
    employment = models.CharField(blank=True, null=True, max_length=250, verbose_name="16- Employment status")
    religion = models.CharField(blank=True, null=True, max_length=250, verbose_name="17- Religious/ideological affiliation")
    mental = models.CharField(blank=True, null=True, max_length=250, verbose_name="18- Mental health diagnoses (personality disorder, schizophrenia/ psychosis, bipolar disorder, major depression)")
    othersample = models.CharField(blank=True, null=True, max_length=250, verbose_name="19- Any other relevant info")
    latent = models.BooleanField(default=False, verbose_name="20- Latent class analysis?")
    cluster = models.BooleanField(default=False, verbose_name="21- Cluster analysis?")
    patha = models.BooleanField(default=False, verbose_name="22- Path analysis/structural equation model analysis?")
    regression = models.BooleanField(default=False, verbose_name="23- Regression?")
    linear = models.BooleanField(default=False, verbose_name="24- Hierarchical linear modeling?")
    discriminat = models.BooleanField(default=False, verbose_name="25- Discriminant analysis?")
    otherquantianalysis = models.BooleanField(default=False, verbose_name="26- Other kind of analysis?")
    otherquantitxt = models.CharField(blank=True, null=True, max_length=250, verbose_name="26a- If Other describe?")
    thematique = models.BooleanField(default=False, verbose_name="27- Thematic?")
    otherqualianalysis = models.BooleanField(default=False, verbose_name="28- Other kind of analysis?")
    otherqualitxt = models.CharField(blank=True, null=True, max_length=250, verbose_name="28a- If Other describe?")
    variable1 = models.BooleanField(default=False, verbose_name="collected during childhood?")
    variable2 = models.BooleanField(default=False, verbose_name="collected during adolescence (12-18 ou 21 ans)?")
    variable3 = models.BooleanField(default=False, verbose_name="collected during adulthood (> 18 ou 21 ans)?")
    variable4 = models.BooleanField(default=False, verbose_name="end in expressive violence?")
    variable5 = models.BooleanField(default=False, verbose_name="end in instrumental violence?")
    variable6 = models.BooleanField(default=False, verbose_name="end in ritualized violence?")
    variable7 = models.BooleanField(default=False, verbose_name="end in non specified violence?")
    trajectoire1 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 1")
    trajectoire2 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 2")
    trajectoire3 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 3")
    trajectoire4 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 4")
    trajectoire5 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 5")
    trajectoire6 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 6")
    trajectoire7 = models.CharField(blank=True, null=True, max_length=250, verbose_name="Trajectoire 7")
    limitations = models.CharField(blank=True, null=True, max_length=250, verbose_name="Limitations")
    sousetude = models.BooleanField(default=False, verbose_name="S'agit-il d'une sous étude ou d'un sous échantillon?")
    etudemere = models.CharField(blank=True, null=True, max_length=250, verbose_name="Si oui référence de l'étude originale et ID")
    RA = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title