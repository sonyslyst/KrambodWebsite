from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from krambod.models import Article, Information, Photo, PhotoTag

def getPrevNext(photos, current, tag):
    makeUrl = lambda ph: (reverse('photos') + (("?tag=" + str(tag) + "&") if tag else "?") + "show=" + str(ph.pk)) if ph else "#"
    i = iter(photos)
    prevPhoto = None;
    for photo in i:
        if photo.pk == current.pk:
            return makeUrl(prevPhoto), makeUrl(next(i, None))
        prevPhoto = photo

class KrambodViewMixin(object):
    def get(self, request, *args, **kwargs):
        self.request = request
        return super(KrambodViewMixin, self).get(request, *args, **kwargs)
    

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
        
class PhotoPageView(TemplateView, KrambodViewMixin):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoPageView, self).get_context_data(**kwargs)

        filterByTag = self.request.GET.get('tag', None)
        context['tag'] = filterByTag
        tag = None
        try: 
            tag = PhotoTag.objects.get(name = filterByTag)
        except:
            context['photos'] = Photo.objects.all()
        else:
            context['photos'] = Photo.objects.filter(tags = tag)

        showPhoto = self.request.GET.get('show', None)
        photo = None
        try: 
            photo = Photo.objects.get(pk = showPhoto)
        except:
            pass
        else:
            context['show_photo'] = photo
            context['previous_url'], context['next_url'] = getPrevNext(context['photos'], photo, tag)

        context['tags'] = PhotoTag.objects.all()
        return context
