from django.urls import path
from .views import post_energy_passport, get_energy_passports, download_energy_passport
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('passport/create', post_energy_passport, name='create-passport'),
    path('passport/list/', get_energy_passports, name='list-passports'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('passport/download/', download_energy_passport, name='download-passport'),
]