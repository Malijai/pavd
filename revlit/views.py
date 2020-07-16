from collections import OrderedDict
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ArticleForm, RechercheForm
from django.contrib.auth.decorators import login_required
from .models import Articles, Volet, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count, Sum, Avg
from django.db import connection


@login_required(login_url=settings.LOGIN_URI)
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.RA = request.user
            article.save()
            volet = request.POST.get('volet')
            messages.success(request, "L'article a été ajouté à la liste")
            return redirect(article_list, volet, 1)
        else:
            messages.error(request, "Il y a eu une erreur dans la création de l'article, recommencez")
    else:
        form = ArticleForm()
    return render(request, 'article_edit.html', {'form': form})


@login_required(login_url=settings.LOGIN_URI)
def accueil(request):

    return render(request, 'accueil.html')


@login_required(login_url=settings.LOGIN_URI)
def article_edit(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            volet = article.volet_id
            messages.success(request, "Les modifications ont été enregistrées")
            if 'Savesurplace' in request.POST:
                return redirect(article_edit, article.id)
            else:
                return redirect(article_list, volet, 1)
        else:
            messages.error(request, "Il y a eu une erreur dans la modification de l'article, recommencez")
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_edit.html', {'form': form})


@login_required(login_url=settings.LOGIN_URI)
def article_list(request, volet, tri=1, ):
    volet = volet
    if tri == 1:
        ordre1 = 'authors'
        ordre2 = 'title'
        ordre3 = 'year'
        ordre4 = 'RA'
    elif tri == 2:
        ordre1 = 'title'
        ordre2 = 'year'
        ordre3 = 'RA'
        ordre4 = 'volet'
    elif tri == 3:
        ordre1 = 'studytype'
        ordre2 = 'title'
        ordre3 = 'year'
        ordre4 = 'volet'
    elif tri == 4:
        ordre1 = 'RA'
        ordre2 = 'termine'
        ordre3 = 'title'
        ordre4 = 'volet'

    if request.user.groups.filter(name='SuperU').exists():
        articles_tous = Articles.objects.filter(volet_id=volet).order_by(ordre1, ordre2, ordre3, ordre4)
        superu = 1
    else:
        articles_tous = Articles.objects.filter(Q(RA=request.user) & Q(volet_id=volet)).order_by(ordre1, ordre2, ordre3, ordre4)
        superu = 0
    levolet = Volet.objects.get(pk=volet)
    paginator = Paginator(articles_tous, 50)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles_list.html', {'articles': articles, 'superu': superu, 'tri': tri,
                                                  'volet': volet, 'voletnom': levolet.reponse })


@login_required(login_url=settings.LOGIN_URI)
def bilan_irr(request, volet):
    toutesleslignesMH = []
    toutesleslignesQ = []
    toutesleslignesMetho = []
    toutesleslignesSample = []
    toutesleslignesTsvr = []
    toutesleslignesPath = []
    toutesleslignesVar = []
    toutesleslignesTipv = []
    with connection.cursor() as cursor:
        text = "select joined.docid from (select a.docid, a.RA_id as RA_a,b.RA_id as RA_b from " \
               "revlit_articles a join revlit_articles b on a.docid = b.docid " \
               "where a.volet_id = " + str(volet) + " and a.termine = 1 and b.termine = 1 " \
               "and a.RA_id < b.RA_id) as joined"
        cursor.execute(text)
        articles_irr = cursor.fetchall()
    for a_irr in articles_irr:
        ligneMH = []
        ligneQ = []
        ligneMetho = []
        ligneSample = []
        ligneTsvr = []
        lignePath = []
        ligneVar = []
        ligneTipv = []
        irrMH = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid')\
            .annotate(cpt1=Sum('categomh1'),cpt2=Sum('categomh2'),cpt3=Sum('categomh3'),
                      cpt4=Sum('categomh4'),cpt5=Sum('categomh5'),cpt6=Sum('categomh6'),
                      cpt7=Sum('categomh7'),cpt8=Sum('categomh8'),compte=Count('docid'))
        nombreirr = irrMH[0]['compte']
        ligneMH.append(a_irr[0])
        ligneMH.append(nombreirr)
        ligneMH.extend([traduitbool(irrMH[0]['cpt1']), traduitbool(irrMH[0]['cpt2']), traduitbool(irrMH[0]['cpt3']), traduitbool(irrMH[0]['cpt4'])])
        ligneMH.extend([traduitbool(irrMH[0]['cpt5']), traduitbool(irrMH[0]['cpt6']), traduitbool(irrMH[0]['cpt7']), traduitbool(irrMH[0]['cpt8'])])
        toutesleslignesMH.append(ligneMH)

        irrQ = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(qs1=Sum('qs1'), qs2=Sum('qs2'), qs3=Sum('qs3'),
                  qs4=Sum('qs4'), qs5=Sum('qs5'), qs7=Sum('qs7'),
                  peer=Sum('peer'))
        ligneQ.append(a_irr[0])
        ligneQ.append(nombreirr)
        ligneQ.extend([traduitbool(irrQ[0]['qs1']),traduitbool(irrQ[0]['qs2']),traduitbool(irrQ[0]['qs3']),traduitbool(irrQ[0]['qs4'])])
        ligneQ.extend([traduitbool(irrQ[0]['qs5']),traduitbool(irrQ[0]['qs7']),traduitbool(irrQ[0]['peer'])])
        toutesleslignesQ.append(ligneQ)

        irrMetho = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(meeting=Sum('meeting'), record=Sum('record'), psychotest=Sum('psychotest'),
                      designquali1=Sum('designquali1'), designquali2=Sum('designquali2'), designquali3=Sum('designquali3'),
                      designquali4=Sum('designquali4'), designquali5=Sum('designquali5'), designquali6=Sum('designquali6'),
                      studytype=Sum('studytype'))
        ligneMetho.append(a_irr[0])
        ligneMetho.append(nombreirr)
        ligneMetho.extend([traduitbool(irrMetho[0]['meeting']), traduitbool(irrMetho[0]['record']), traduitbool(irrMetho[0]['psychotest']),
                          traduitbool(irrMetho[0]['designquali1']), traduitbool(irrMetho[0]['designquali2']), traduitbool(irrMetho[0]['designquali3']),
                          traduitbool(irrMetho[0]['designquali4']), traduitbool(irrMetho[0]['designquali5']), traduitbool(irrMetho[0]['designquali6']),
                          traduitbool(irrMetho[0]['studytype'])])
        toutesleslignesMetho.append(ligneMetho)

        irrSample = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(a=Sum('provenanceh'), b=Sum('provenancep'), c=Sum('provenancec'), d=Sum('provenancecp'), e=Sum('provenanceo'),
                      f=Sum('provenanceunk'))
        ligneSample.append(a_irr[0])
        ligneSample.append(nombreirr)
        ligneSample.extend([traduitbool(irrSample[0]['a']),traduitbool(irrSample[0]['b']),traduitbool(irrSample[0]['c']),traduitbool(irrSample[0]['d']),
                            traduitbool(irrSample[0]['e']),traduitbool(irrSample[0]['f'])])
        toutesleslignesSample.append(ligneSample)

        irrAtcdts = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(a=Sum('atcdtsex'),b=Sum('atcdtviol'),c=Sum('noatcdt'),d=Sum('unkatcdt'),e=Sum('victrel1'),f=Sum('victrel2'),g=Sum('victrel3'))
        ligneTsvr.append(a_irr[0])
        ligneTsvr.append(nombreirr)
        ligneTsvr.extend([traduitbool(irrAtcdts[0]['a']),traduitbool(irrAtcdts[0]['b']),traduitbool(irrAtcdts[0]['c']),traduitbool(irrAtcdts[0]['d']),
                            traduitbool(irrAtcdts[0]['e']),traduitbool(irrAtcdts[0]['f']),traduitbool(irrAtcdts[0]['g'])])
        toutesleslignesTsvr.append(ligneTsvr)

        irrPath = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(a=Sum('latent'), b=Sum('cluster'), c=Sum('patha'), d=Sum('regression'), e=Sum('linear'), f=Sum('discriminat'),
                      g=Sum('otherquantianalysis'), h=Sum('thematique'), i=Sum('otherqualianalysis'))
        lignePath.append(a_irr[0])
        lignePath.append(nombreirr)
        lignePath.extend([traduitbool(irrPath[0]['a']),traduitbool(irrPath[0]['b']),traduitbool(irrPath[0]['c']),traduitbool(irrPath[0]['d']),
                          traduitbool(irrPath[0]['e']),traduitbool(irrPath[0]['f']),traduitbool(irrPath[0]['g']),traduitbool(irrPath[0]['h']),traduitbool(irrPath[0]['i'])])
        toutesleslignesPath.append(lignePath)

        irrVar = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(h=Sum('variable1'), i=Sum('variable2'), j=Sum('variable3'), k=Sum('variable4'), l=Sum('variable5'),
                      m=Sum('variable6'), n=Sum('variable7'), o=Sum('variable8'))
        ligneVar.append(a_irr[0])
        ligneVar.append(nombreirr)
        ligneVar.extend([traduitbool(irrVar[0]['h']), traduitbool(irrVar[0]['i']),traduitbool(irrVar[0]['j']),
                         traduitbool(irrVar[0]['k']),traduitbool(irrVar[0]['l']), traduitbool(irrVar[0]['m']),
                         traduitbool(irrVar[0]['n']),traduitbool(irrVar[0]['o'])])
        toutesleslignesVar.append(ligneVar)
        irrTipv = Articles.objects.values('docid').filter(Q(docid=a_irr[0])).order_by('docid') \
            .annotate(h=Sum('married'), i=Sum('commited'), j=Sum('domestic'), k=Sum('openr'), l=Sum('divorced'),
                      m=Sum('cohab'))
        ligneTipv.append(a_irr[0])
        ligneTipv.append(nombreirr)
        ligneTipv.extend([traduitbool(irrTipv[0]['h']), traduitbool(irrTipv[0]['i']),traduitbool(irrTipv[0]['j']),
                         traduitbool(irrTipv[0]['k']),traduitbool(irrTipv[0]['l']), traduitbool(irrTipv[0]['m'])])
        toutesleslignesTipv.append(ligneTipv)

    return render(request, 'articles_irr.html', {
                                                 'lignesMH9': toutesleslignesMH,
                                                 'lignesQ8': toutesleslignesQ,
                                                 'lignesMetho11': toutesleslignesMetho,
                                                 'lignesSample7': toutesleslignesSample,
                                                 'lignesTsvr8': toutesleslignesTsvr,
                                                 'lignesPath10': toutesleslignesPath,
                                                 'lignesVar9': toutesleslignesVar,
                                                 'lignesTipv7': toutesleslignesTipv,
                                                 'volet':volet
                                                 })


def traduitbool(val):
    valbool = "-"
    if str(val) == "True":
        valbool = 1
    elif str(val) == "False":
        valbool = 0
    elif str(val) == "NULL":
        valbool = ""
    else:
        valbool = val
    return valbool


def cherche_article(request, doc, volet):
    article_ras = Articles.objects.values('RA').filter(docid=doc, volet=volet).order_by('RA')
    comparaison = OrderedDict()
    liste_ras = []
    for ra in article_ras:
        articles = Articles.objects.filter(docid=doc, RA_id=ra['RA'], volet=volet)
        fields = articles.model._meta.fields
        liste_ras.append(ra['RA'])
        for field in fields:
            # print(field.attname)
            value = tuple([ra['RA'], articles.values()[0][field.attname]])
            if field.attname == "volet_id" or \
               field.attname == "type_id" or \
               field.attname == "studytype_id" or \
               field.attname == "eligiblesr" or \
               field.attname == "designquanti1" or \
               field.attname == "designquanti2" or \
               field.__class__.__name__ == "BooleanField":
                if field.verbose_name not in comparaison:
                    comparaison[field.verbose_name] = [value]
                    #print(field.verbose_name)
                    #print(field.__class__.__name__)
                else:
                    comparaison[field.verbose_name].append(value)
    #print(liste_ras)
    users = User.objects.filter(pk__in=liste_ras).order_by('id')

    return render(request, 'articles_verifie.html', {
                                                 'article_ra':article_ras,
                                                 'articles': articles,
                                                 'lignes': comparaison,
                                                 'users': users,
                                                 'volet': volet,
                                                 })


def recherche(request):
    form_rech = RechercheForm
    if request.method == 'POST':
        form = form_rech(data=request.POST)
        if form.is_valid():
            volet = request.POST.get('volet', '')
            titre = request.POST.get('recherchetitre', '')
            auteur = request.POST.get('rechercheauteur', '')
            requete = Q(volet__id=volet)
            if titre:
                requete = Q(title__icontains=titre) & requete
            if auteur:
                requete = Q(authors__icontains=auteur) & requete
            articles = Articles.objects.filter(requete)
            if articles:
                return render(request, 'articles_list.html', {'articles': articles, 'superu': 1})
            else:
                message = ("Cet auteur - {} - ou cette expression - {} - n'ont pas été trouvés dans les articles rentrés du volet"
                           " - {} -").format(auteur,titre, volet)
                return render(request, 'Recherche.html', {'form': form, 'message': message})
    else:
        form_rech = RechercheForm()

    return render(request, 'Recherche.html', {'form': form_rech})
