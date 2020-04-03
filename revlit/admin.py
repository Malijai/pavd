from django.contrib import admin
from .models import Typepub, Typestud, Quanti, Articles


class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "designquanti1":
            kwargs["queryset"] = Quanti.objects.filter(catego=1)
        elif db_field.name == "designquanti2":
            kwargs["queryset"] = Quanti.objects.filter(catego=2)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = [
        ('Identification', {'fields': ['docid', 'title', 'authors', 'peer', ('year', 'type', 'othertype')]}),
        ('Data source (cocher si oui)', {'fields': [('meeting', 'record'), ('psychotest', 'otherdata')]}),
        ('Study type', {'fields': ['studytype']}),
        ('9 - Study type if quantitative', {'fields': [('designquanti1','designquanti2')]}),
        ('10 - Study type if qualitative', {'fields': [('designquali1', 'designquali2','designquali3', 'designquali4', 'designquali5',),
                                                  ('designquali6','otherqual')]}),
        ('Sample characteristics', {'fields': [('nparticipant', 'ratiomf'), ('age', 'ethno'),
                                               ('education', 'employment'), ('religion', 'mental'), 'othersample']}),
        ('Data analysis (methods used to extract trajectories) - quantitative (cocher si oui)',
            {'fields': [('latent', 'cluster', 'patha'), ('regression', 'linear', 'discriminat'),
                        ('otherquantianalysis', 'otherquantitxt')]}),
        ('Data analysis(methods used to extract trajectories) - qualitative (cocher si oui)',
            {'fields': ['thematique', ('otherqualianalysis', 'otherqualitxt')]}),
        ('Variables (cocher si oui)', {'fields': [('variable1', 'variable2', 'variable3'), ('variable4', 'variable5', 'variable6', 'variable7')]}),
        ('Trajectories', {'fields': ['trajectoire1', 'trajectoire2', 'trajectoire3', 'trajectoire4', 'trajectoire5', 'trajectoire6', 'trajectoire7']}),
        ('Autres informations', {'fields': ['limitations', 'sousetude', 'etudemere']}),
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
admin.site.register(Quanti)
