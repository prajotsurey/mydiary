from django.shortcuts import render,redirect
from . models import Article
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = "accounts/login/")
def article_list (request):
	username = request.user
	articles = Article.objects.all().order_by('-date')
	return render(request,'articles/article_list.html',{'articles':articles,'request':request})

@login_required(login_url = "accounts/login/")
def article_create(request):
	if request.method == 'POST':
		form = forms.Create_Article(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()
			return redirect('articles:list')
	else:
		form  = forms.Create_Article()
	return render(request,'articles/article_create.html',{'form': form})

def article_detail(request,slug):
	article = Article.objects.get(slug = slug)
	return render(request,'articles/article_detail.html',{'article' : article})

def home(request):
	return render(request,'articles/homepage.html')