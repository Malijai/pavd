from __future__ import unicode_literals
from django import template
import re

register = template.Library()


@register.simple_tag
def fait_different(valeurs):
    comp = ()
    ligne = ''
    old = ''
    for valeur in valeurs:
        if valeur[1] is None:
            val = ''
        else:
            val = valeur[1]
        if old == '':
            old = val
        if val == old:
            ligne += "<td>" + str(val) + "</td>"
        else:
            ligne += "<td><b>" + str(val) + "</b></td>"
        old = val

    return ligne