from django.shortcuts import render, get_object_or_404
from .models import Blog


def home(request):
	blogs = Blog.objects.all()[::-1]
	context = {
		'blogs': blogs,
	}
	return render(request, 'blog/home.html', context)


def single_blog(request, blog_id):
	blog = get_object_or_404(Blog, id=blog_id)
	all_blogs = Blog.objects.all()[::-1]
	context = {
		'blog':blog,
		'blogs': all_blogs,
	}
	return render(request, 'blog/single_blog.html', context)


def about(request):
	return render(request, 'blog/about.html')

def resource(request):
	return render(request, 'blog/resource.html')

def mailing(request):
	return render(request, 'blog/mailing.html')


