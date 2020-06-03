from __future__ import unicode_literals
from django import template
import re

register = template.Library()


@register.simple_tag
def fait_different(valeurs):
    delim_pareils = "</td><td>"
    debut_pareils = "<td>"
    couleur = 'class="w3-amber"'
    delim_differents = '</td><td {}>'.format(couleur)
    debut_differents = '<td {}>'.format(couleur)
    old = ''
    pareils = True
    formatte = []
    for valeur in valeurs:
        if valeur[1] is None:
            val = ''
        else:
            val = valeur[1]
        if old == '':
            old = val
        if val != old:
            pareils = False
        formatte.append(str(val))
        old = val

    return debut_pareils + delim_pareils.join(formatte) + "</td>" if pareils \
        else debut_differents + delim_differents.join(formatte) + "</td>"