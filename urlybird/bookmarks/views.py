from django.shortcuts import render
from django.views import generic
from .models import Worm, Click

# Create your views here.


class BirdIndexView(generic.ListView):
    template_name = 'bookmarks/all_worms.html'
    context_object_name = 'all_worms'
    paginate_by = 25

    def get_queryset(self):
        return Worm.objects.all().order_by('-timestamp')


class WormIndexView(generic.ListView):
    template_name = 'bookmarks/bird_detail.html'
    context_object_name = 'all_worms'
    paginate_by = 25

    def get_queryset(self):
        return self.user.rating_set.all().order_by('-timestamp')


class WormDetailView(generic.DetailView):
    model = Worm
    template = 'bookmarks/worm_detail.html'
