from django.contrib.auth import logout, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.forms import RegisterForm, LoginForm, ArticleForm, CommentForm
from blog.models import Article, Comment


# Create your views here.
# def home(request):
#     articles = Article.objects.all()
#     # articles = Article.objects.filter(publish=True)
#     context = {
#         "articles":articles,
#         "title":"Home"
#     }
#     return render(request, "blog/home.html", context)

class ArticleView(ListView):
    model = Article
    template_name = "blog/home.html"
    context_object_name = "articles"
    extra_context = {
        "title": "Home"
    }
    def get_queryset(self):
        return Article.objects.filter(publish=True)


# def article_by_category(request, pk):
#     articles = Article.objects.filter(category_id=pk)
#     context = {
#         "title":"Category",
#         "articles":articles
#     }
#     return render(request, "blog/home.html", context)

class ArticleByCategory(ArticleView):
    extra_context = {
        "title":"Category"
    }
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs["pk"])

# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = CommentForm()
#
#     context = {
#         "title":"Detail",
#         "article":article,
#         "form":form
#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/detail.html"
    form_class = CommentForm
    extra_context = {
        "title":"Detail"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=article)
        context['form'] = CommentForm()
        return context

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    context = {
        "title":"Register",
        "form":form
    }
    return render(request, "blog/register.html", context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    context = {
        "title":"Login",
        "form":form
    }
    return render(request, "blog/login.html", context)

def user_logout(request):
    logout(request)
    return redirect("home")

def user_profile(request):
    context = {
        "title":"Profile"
    }
    return render(request, "blog/profile.html", context)

class AddArticle(CreateView):
    model = Article
    template_name = "blog/add_article.html"
    form_class = ArticleForm
    extra_context = {
        "title":"Add Article"
    }

class EditArticle(UpdateView):
    model = Article
    template_name = "blog/add_article.html"
    form_class = ArticleForm
    extra_context = {
        "title":"Add Article"
    }

class DeleteArticle(DeleteView):
    model = Article
    context_object_name = "article"
    success_url = reverse_lazy('home')
    extra_context = {
        "title":"Delete"
    }

def save_comment(request, pk):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = Article.objects.get(pk=pk)
        comment.save()
    else:
        pass
    return redirect('detail', pk)

class SearchResult(ArticleView):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(
            Q(title__icontains=word), publish=True
        )
        return articles