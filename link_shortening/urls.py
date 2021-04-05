from django.urls import path
from link_shortening.views import main, redirect_original

urlpatterns = [
    path('', main, name='main'),
    path('<int:short_id>', redirect_original, name='redirect_original'),
]