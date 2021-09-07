from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import photoView, photodelview

#router = DefaultRouter()
#router.register('galleryapi', photoView, basename='galleryapi')

urlpatterns = [
    path('galleryapi/', photoView.as_view()),
    path('photodelapi/<int:pk>', photodelview.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)