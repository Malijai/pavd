from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categomh(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    reponse = models.CharField(max_length=200, )

    def __str__(self):
        return '%s' % self.reponse


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


class Articles(models.Model):
    Yes = 'Yes'
    No = 'No'
    Maybe = 'Maybe'
    BOOL_CHOICES = [
        (Yes, 'Yes'),
        (No, 'No'),
        (Maybe, 'Maybe'),
    ]
    CS = 'Cross-sectional'
    Long = 'Longitudinal'
    DES1_CHOICES = [
        (CS, 'Cross-sectional'),
        (Long, 'Longitudinal'),
    ]
    Retro = 'Retrospective'
    Pro = 'Prospective'
    DES2_CHOICES = [
        (Retro, 'Retrospective'),
        (Pro, 'Prospective'),
    ]
    docid = models.IntegerField(blank=True, null=True, verbose_name="1- Document ID",)
    categomh = models.ForeignKey(Categomh, null=True,blank=True, on_delete=models.DO_NOTHING, verbose_name="Categories MH", help_text="Obligatoire")
    title = models.CharField(max_length=250, verbose_name="2- Title", help_text="Obligatoire")
    authors = models.CharField(max_length=250, verbose_name="3- Authors (follow APA format)", help_text="Obligatoire")
    year = models.IntegerField(verbose_name="4- Year", help_text="Obligatoire")
    type = models.ForeignKey(Typepub, null=True,blank=True, on_delete=models.DO_NOTHING, verbose_name="5- Place published or accessed")
    othertype = models.CharField(blank=True, null=True, max_length=250, verbose_name="5a- If other specify")
    peer = models.BooleanField(default=False, verbose_name="6- Peer reviewed (check if Yes)?")
    qs1 = models.BooleanField(default=False, verbose_name="QS1- Are the key concepts and variables clearly defined?")
    qs2 = models.BooleanField(default=False, verbose_name="QS2- Are the research questions/hypotheses clearly stated?")
    qs3 = models.BooleanField(default=False, verbose_name="QS3- Is the sample adequately described?")
    qs4 = models.BooleanField(default=False, verbose_name="QS4- Are there enough methodological details (can the study be reproduced)?")
    qs5 = models.BooleanField(default=False, verbose_name="QS5- Were major limitations mentioned?")
    qs6 = models.TextField(blank=True, null=True, verbose_name="QS6- Limits identified by the team")
    qs7 = models.BooleanField(default=False, verbose_name="QS7- Is the method adequate to identify pathways?")
    qs1t = models.TextField(blank=True, null=True, verbose_name="QS1-txt- Comments")
    qs2t = models.TextField(blank=True, null=True, verbose_name="QS2-txt- Comments")
    qs3t = models.TextField(blank=True, null=True, verbose_name="QS3-txt- Comments")
    qs4t = models.TextField(blank=True, null=True, verbose_name="QS4-txt- Comments")
    qs5t = models.TextField(blank=True, null=True, verbose_name="QS5-txt- Comments")
    qs7t = models.TextField(blank=True, null=True, verbose_name="QS7-txt- Comments")
    eligiblesr = models.CharField(max_length=6, blank=True, null=True, choices=BOOL_CHOICES, verbose_name="Is the paper eligible for the S.R.?")
    meeting = models.BooleanField(default=False, verbose_name="7a- Meetings with participants?")
    record = models.BooleanField(default=False, verbose_name="7b- Records?")
    psychotest = models.BooleanField(default=False, verbose_name="7c Presence of psychometric tests?")
    otherdata = models.CharField(blank=True, null=True, max_length=250, verbose_name="7c1- List of psychometric tests (if applicable)")
    studytype = models.ForeignKey(Typestud, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name="8- Study type")
    designquanti1 = models.CharField(max_length=15, blank=True, null=True, choices=DES1_CHOICES, verbose_name="9a- Study design (if quantitative)")
    designquanti2 = models.CharField(max_length=15, blank=True, null=True, choices=DES2_CHOICES, verbose_name="9b- Study design (if quantitative)")
    designquali1 = models.BooleanField(default=False, verbose_name="10a- Interview")
    designquali2 = models.BooleanField(default=False, verbose_name="10b- Focus groups")
    designquali3 = models.BooleanField(default=False, verbose_name="10c- Observation")
    designquali4 = models.BooleanField(default=False, verbose_name="10d- Ethnography")
    designquali5 = models.BooleanField(default=False, verbose_name="10e- Case study")
    designquali6 = models.BooleanField(default=False, verbose_name="10f- Other")
    otherqual = models.CharField(blank=True, null=True, max_length=100, verbose_name="10a- If other specify (ex. structured clinical judgment):")
    nparticipant = models.CharField(blank=True, null=True, max_length=250, verbose_name="11- Number of participants")
    ratiomf = models.CharField(blank=True, null=True, max_length=250, verbose_name="12- Males / Females")
    age = models.CharField(blank=True, null=True, max_length=250, verbose_name="13- Ages")
    paysrecrut = models.CharField(blank=True, null=True, max_length=250, verbose_name="1---- Country where data was collected")
    ethno = models.CharField(blank=True, null=True, max_length=250, verbose_name="14- Ethno-racial group")
    education = models.CharField(blank=True, null=True, max_length=250, verbose_name="15- Education")
    employment1 = models.CharField(blank=True, null=True, max_length=250, verbose_name="16- Employment status #1")
    employment2 = models.CharField(blank=True, null=True, max_length=250, verbose_name="16- Employment status #2")
    employment3 = models.CharField(blank=True, null=True, max_length=250, verbose_name="16- Employment status #3")
    employment4 = models.CharField(blank=True, null=True, max_length=250, verbose_name="16- Employment status #4")
    employmentw1 = models.CharField(blank=True, null=True, max_length=250, verbose_name="When? #1")
    employmentw2 = models.CharField(blank=True, null=True, max_length=250, verbose_name="When? #2")
    employmentw3 = models.CharField(blank=True, null=True, max_length=250, verbose_name="When? #3")
    employmentw4 = models.CharField(blank=True, null=True, max_length=250, verbose_name="When? #4")
    religion = models.CharField(blank=True, null=True, max_length=250, verbose_name="17- Religious/ideological affiliation")
    mental = models.CharField(blank=True, null=True, max_length=250, verbose_name="18- Mental health diagnoses (personality disorder, schizophrenia/ psychosis, bipolar disorder, major depression)")
    provenanceh = models.BooleanField(default=False, verbose_name="Sample provenance: Hospital?")
    provenancep = models.BooleanField(default=False, verbose_name="Sample provenance: Prison/penitentiary?")
    provenancec = models.BooleanField(default=False, verbose_name="Sample provenance: Community?")
    provenancecp = models.BooleanField(default=False, verbose_name="Sample provenance: Community-based program?")
    provenanceo = models.BooleanField(default=False, verbose_name="Sample provenance: Other?")
    provenanceunk = models.BooleanField(default=False, verbose_name="Sample provenance: Not specified?")
    provenanceht = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    provenancept = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    provenancect = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    provenancecpt = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    provenanceot = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    provenanceunkt = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    othersamplns = models.CharField(blank=True, null=True, max_length=250, verbose_name="19- Any other relevant info")
    atcdtsex = models.BooleanField(default=False, verbose_name="Sexual antecedents?")
    atcdtviol = models.BooleanField(default=False, verbose_name="Violent antecedents?")
    noatcdt = models.BooleanField(default=False, verbose_name="No sexual, no violent antecedents?")
    unkatcdt = models.BooleanField(default=False, verbose_name="Not specified?")
    atcdtsext = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    atcdtviolt = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    noatcdtt = models.CharField(blank=True, null=True, max_length=250, verbose_name=" % of the sample")
    unkatcdtt = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    victgender = models.CharField(blank=True, null=True, max_length=250, verbose_name="Victims: Male/Female")
    victage = models.CharField(blank=True, null=True, max_length=250, verbose_name="Victims: Age")
    victrel1 = models.BooleanField(default=False, verbose_name="Relation with the victim: Intrafamilial?")
    victrel1t = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    victrel2 = models.BooleanField(default=False, verbose_name="Relation with the victim: Extrafamilial?")
    victrel2t = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
    victrel3 = models.BooleanField(default=False, verbose_name="Relation with the victim: Not specified")
    victrel3t = models.CharField(blank=True, null=True, max_length=250, verbose_name="% of the sample")
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
    variable1 = models.BooleanField(default=False, verbose_name="Were there variables in the trajectories during childhood?")
    variable2 = models.BooleanField(default=False, verbose_name="Were there variables in the trajectories during adolescence?")
    variable3 = models.BooleanField(default=False, verbose_name="Were there variables in the trajectories during adulthood?")
    variable4 = models.BooleanField(default=False, verbose_name="Did some trajectories end in expressive violence?")
    variable5 = models.BooleanField(default=False, verbose_name="Did some trajectories end in instrumental violence?")
    variable6 = models.BooleanField(default=False, verbose_name="Did some trajectories end in ritualized violence?")
    variable7 = models.BooleanField(default=False, verbose_name="Did some trajectories end in non specified violence?")
    variable8 = models.BooleanField(default=False, verbose_name="Not specified")
    variable1t = models.CharField(blank=True, null=True, max_length=250, verbose_name="Variables in the trajectories during childhood")
    variable2t = models.CharField(blank=True, null=True, max_length=250, verbose_name="Variables in the trajectories during adolescence")
    variable3t = models.CharField(blank=True, null=True, max_length=250, verbose_name="Variables in the trajectories during adulthood")
    variable4t = models.CharField(blank=True, null=True, max_length=250, verbose_name="End in expressive violence")
    variable5t = models.CharField(blank=True, null=True, max_length=250, verbose_name="End in instrumental violence")
    variable6t = models.CharField(blank=True, null=True, max_length=250, verbose_name="End in ritualized violence")
    variable7t = models.CharField(blank=True, null=True, max_length=250, verbose_name="End in non specified violence")
    variable8t = models.CharField(blank=True, null=True, max_length=250, verbose_name="Not specified")
    variable9 = models.TextField(blank=True, null=True, verbose_name="List of variables used in the trajectories")
    trajectoire1 = models.TextField(blank=True, null=True, verbose_name="Trajectory 1")
    trajectoire2 = models.TextField(blank=True, null=True, verbose_name="Trajectory 2")
    trajectoire3 = models.TextField(blank=True, null=True, verbose_name="Trajectory 3")
    trajectoire4 = models.TextField(blank=True, null=True, verbose_name="Trajectory 4")
    trajectoire5 = models.TextField(blank=True, null=True, verbose_name="Trajectory 5")
    trajectoire6 = models.TextField(blank=True, null=True, verbose_name="Trajectory 6")
    trajectoire7 = models.TextField(blank=True, null=True, verbose_name="Trajectory 7")
    smtvt1 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 1")
    smtvt2 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 2")
    smtvt3 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 3")
    smtvt4 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 4")
    smtvt5 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 5")
    smtvt6 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 6")
    smtvt7 = models.TextField(blank=True, null=True, verbose_name="Shift markers towards violence of trajectory 7")
    limitations = models.TextField(blank=True, null=True, verbose_name="Limitations")
    sousetude = models.BooleanField(default=False, verbose_name="S'agit-il d'une sous étude ou d'un sous échantillon?")
    etudemere = models.CharField(blank=True, null=True, max_length=250, verbose_name="Si oui référence de l'étude originale (et ID si connu)")
    RA = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    termine = models.BooleanField(default=False, verbose_name="Check if the codification of the paper is finished")

    class Meta:
        ordering = ['authors', 'title', 'year']
        unique_together = (('authors', 'title', 'year','RA'),)

    def __str__(self):
        return '%s' % self.title