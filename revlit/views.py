from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url=settings.LOGIN_URI)
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.RA = request.user
            article.save()
            messages.success(request, "L'article a été ajouté à la liste")
            return redirect('article_list')
        else:
            messages.error(request, "Il y a eu une erreur dans la création de l'article, recommencez")
    else:
        form = ArticleForm()
    return render(request, 'article_edit.html', {'form': form})


@login_required(login_url=settings.LOGIN_URI)
def article_edit(request, pk):
    article = Articles.objects.get(pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            messages.success(request, "Les modifications ont été enregistrées")
            if 'Savesurplace' in request.POST:
                return redirect(article_edit, article.id)
            else:
                return redirect('article_list')
        else:
            messages.error(request, "Il y a eu une erreur dans la modification de l'article, recommencez")
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_edit.html', {'form': form})


@login_required(login_url=settings.LOGIN_URI)
def article_list(request):
    articles_tous = Articles.objects.all().order_by('authors', 'title', 'year')
    paginator = Paginator(articles_tous, 100)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'articles_list.html', {'articles': articles})



