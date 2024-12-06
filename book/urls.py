from django.urls import path, include
from .views import BookView, PublisherView, AuthoreView, CategoryView
from rest_framework.routers import DefaultRouter
from spyne.server.django import DjangoView
from .soap_service import application

router = DefaultRouter()
router.register(r'publisher', PublisherView, basename='publisher')
router.register(r'category', CategoryView, basename='category')
router.register(r'authore', AuthoreView, basename='authore')
router.register(r'books', BookView, basename='books')


soap_path = [
    path('', DjangoView.as_view(application=application)),
]

urlpatterns = [
    path('soap/', include(soap_path)),
]


urlpatterns += router.urls