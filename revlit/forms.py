# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Articles


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['termine'].widget.attrs.update({'class': 'checkmod'})
        self.fields['designquali1'].widget.attrs.update({'class': 'checkmod'})
        self.fields['designquali2'].widget.attrs.update({'class': 'checkmod'})
        self.fields['designquali3'].widget.attrs.update({'class': 'checkmod'})
        self.fields['designquali4'].widget.attrs.update({'class': 'checkmod'})
        self.fields['designquali5'].widget.attrs.update({'class': 'checkmod'})
        self.fields['designquali6'].widget.attrs.update({'class': 'checkmod'})
        self.fields['latent'].widget.attrs.update({'class': 'checkmod'})
        self.fields['cluster'].widget.attrs.update({'class': 'checkmod'})
        self.fields['patha'].widget.attrs.update({'class': 'checkmod'})
        self.fields['regression'].widget.attrs.update({'class': 'checkmod'})
        self.fields['linear'].widget.attrs.update({'class': 'checkmod'})
        self.fields['discriminat'].widget.attrs.update({'class': 'checkmod'})
        self.fields['otherquantianalysis'].widget.attrs.update({'class': 'checkmod'})
        self.fields['thematique'].widget.attrs.update({'class': 'checkmod'})
        self.fields['otherqualianalysis'].widget.attrs.update({'class': 'checkmod'})
    class Meta:
        model = Articles
        fields = ['termine','docid', 'categomh', 'title', 'authors', 'peer', 'year', 'type', 'othertype','qs1', 'qs1t','qs2', 'qs2t',
            'qs3', 'qs3t', 'qs4', 'qs4t', 'qs5', 'qs5t', 'qs7', 'qs7t', 'qs6','eligiblesr', 'meeting', 'record', 'psychotest',
            'otherdata','studytype','designquanti1','designquanti2','designquali1',
            'designquali2','designquali3', 'designquali4', 'designquali5','designquali6','otherqual','nparticipant',
            'ratiomf','age', 'ethno', 'paysrecrut','education', 'religion','employment1', 'employmentw1','employment2',
            'employmentw2','employment3', 'employmentw3','employment4', 'employmentw4','mental','provenanceh',
            'provenanceht','provenancep','provenancept','provenancec','provenancect','provenancecp','provenancecpt',
            'provenanceo','provenanceot', 'provenanceunk','provenanceunkt','othersamplns','atcdtsex', 'atcdtsext','atcdtviol','atcdtviolt',
            'noatcdt', 'noatcdtt','unkatcdt', 'unkatcdtt','victgender', 'victage', 'victrel1', 'victrel1t',
            'victrel2', 'victrel2t','victrel3', 'victrel3t','latent', 'cluster', 'patha','regression', 'linear', 'discriminat',
            'otherquantianalysis', 'otherquantitxt','thematique', 'otherqualianalysis', 'otherqualitxt','variable1', 'variable1t','variable2', 'variable2t',
            'variable3', 'variable3t','variable4', 'variable4t','variable5','variable5t','variable6', 'variable6t',
            'variable7', 'variable7t','variable8', 'variable8t','variable9','trajectoire1', 'trajectoire2', 'trajectoire3', 'trajectoire4',
            'trajectoire5', 'trajectoire6', 'trajectoire7','smtvt1', 'smtvt2', 'smtvt3', 'smtvt4', 'smtvt5', 'smtvt6', 'smtvt7','sousetude', 'etudemere','inclussr','tsvrrelevant','trajrelevant']
        exclude = ('RA', 'created_at', 'updated_at')

