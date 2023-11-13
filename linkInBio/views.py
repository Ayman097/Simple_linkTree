from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, Link
# Create your views here.

class index(ListView):
    model = Link
    
class LinkCreateView(CreateView):
    model = Link
    fields = '__all__'
    success_url = reverse_lazy('home')

class UpdateLinkView(UpdateView):
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('home')


class DeleteLinkView(DeleteView):
    model = Link
    success_url = reverse_lazy('home')

def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    print(profile)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }

    return render(request, 'linkInBio/profile.html', context)