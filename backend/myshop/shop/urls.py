from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CitemsViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'citems', CitemsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
