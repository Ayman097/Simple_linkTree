from django.urls import path
from .views import index, LinkCreateView, UpdateLinkView, DeleteLinkView, profile_view

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('link/create/', LinkCreateView.as_view(), name='link-create'),
    path('link/<int:pk>/update/', UpdateLinkView.as_view(), name='link-update'),
    path('link/<int:pk>/delete/', DeleteLinkView.as_view(), name='link-delete'),
    path('<slug:profile_slug>/', profile_view, name='profile'),
]