from django.shortcuts import render
from django.views.generic.base import TemplateView

from krambod.models import Article, Information, Photo, PhotoTag

class HomePageView(TemplateView):
	template_name = 'hjem.html'
	
	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		context['articles'] = Article.objects.all()
		return context
		
class InfoPageView(TemplateView):
	template_name = 'Information.html'
	
	def get_context_data(self, **kwargs):
		context = super(InfoPageView, self).get_context_data(**kwargs)
		context['information'] = Information.objects.all()[0]
		return context
		
class PhotoPageView(TemplateView):
	template_name = 'photo.html'

	def get_context_data(self, **kwargs):
		context = super(PhotoPageView, self).get_context_data(**kwargs)
		context['photos'] = Photo.objects.all()
		context['tags'] = PhotoTag.objects.all()
		return context
