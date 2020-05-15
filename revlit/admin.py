from django.contrib import admin
from .models import Typepub, Typestud, Articles, Categomh


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': ['docid', 'categomh', 'title', 'authors', 'peer', ('year', 'type', 'othertype')]}),
        ('Quality of study', {'fields': [('qs1', 'qs1t'), ('qs2', 'qs2t'), ('qs3', 'qs3t'),
                                         ('qs4', 'qs4t'), ('qs5', 'qs5t'), ('qs7', 'qs7t'),'qs6']}),
        ('Is the paper eligible for the S.R.?', {'fields': ['eligiblesr']}),
        ('Data source (check if yes)', {'fields': [('meeting', 'record'), ('psychotest', 'otherdata')]}),


        ('Study type', {'fields': ['studytype']}),
        ('9 - Study design if quantitative', {'fields': [('designquanti1','designquanti2')]}),
        ('10 - Study design if qualitative', {'fields': [('designquali1', 'designquali2','designquali3', 'designquali4', 'designquali5',),
                                                  ('designquali6','otherqual')]}),


        ('Sample characteristics', {'fields': [('nparticipant', 'ratiomf'), ('age', 'ethno', 'paysrecrut'),
                                               ('education', 'religion'),
                                               ('employment1', 'employmentw1'),
                                               ('employment2', 'employmentw2'),
                                               ('employment3', 'employmentw3'),
                                               ('employment4', 'employmentw4'),
                                               'mental',
                                               ('provenanceh', 'provenanceht'),
                                               ('provenancep','provenancept'),
                                               ('provenancec','provenancect'),
                                               ('provenancecp','provenancecpt'),
                                               ('provenanceo','provenanceot'),
                                               ('provenanceunk','provenanceunkt'),
                                               'othersamplns']}),
        ('Data specific to TSVR',{'fields': [('atcdtsex', 'atcdtsext'),
                                             ('atcdtviol','atcdtviolt'),
                                             ('noatcdt', 'noatcdtt'),
                                             ('unkatcdt', 'unkatcdtt'),
                                             'victgender', 'victage', ('victrel1', 'victrel1t'),
                                             ('victrel2', 'victrel2t'),
                                             ('victrel3', 'victrel3t')
                                             ]}),
         ('Data analysis (methods used to extract trajectories) - quantitative (check if yes)',
            {'fields': [('latent', 'cluster', 'patha'), ('regression', 'linear', 'discriminat'),
                        ('otherquantianalysis', 'otherquantitxt')]}),
        ('Data analysis(methods used to extract trajectories) - qualitative (check if yesi)',
            {'fields': ['thematique', ('otherqualianalysis', 'otherqualitxt')]}),
        ('Variables (check if yes)', {'fields': [('variable1', 'variable1t'), ('variable2', 'variable2t'),
                                                 ('variable3', 'variable3t'), ('variable4', 'variable4t'),
                                                 ('variable5','variable5t'), ('variable6', 'variable6t'),
                                                 ('variable7', 'variable7t'), ('variable8', 'variable8t'),
                                                 'variable9']}),
        ('Trajectories', {'fields': ['trajectoire1', 'trajectoire2', 'trajectoire3', 'trajectoire4', 'trajectoire5', 'trajectoire6', 'trajectoire7']}),
        ('Data specific to V.R.', {
            'fields': ['smtvt1', 'smtvt2', 'smtvt3', 'smtvt4', 'smtvt5', 'smtvt6', 'smtvt7']}),
        ('Other informations', {'fields': ['sousetude', 'etudemere']}),
    ]

    list_display = ('docid', 'title', 'authors', 'year')

    ordering = ('title',)

    list_filter = ['year','authors', 'RA']

    search_fields = ('title', 'authors')


    def save_model(self, request, obj, form, change):
        if getattr(obj, 'RA', None) is None:
            obj.RA = request.user
        obj.save()


def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Articles, ArticleAdmin)
admin.site.register(Typepub)
admin.site.register(Typestud)
admin.site.register(Categomh)


