from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductDummyApiView, product_list

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("dummy/", ProductDummyApiView.as_view()),
    path('list/', product_list),
]
