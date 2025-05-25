from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    product_list_create,  # Function-based view
    ProductUpdateView,   # Class-based view
    ProductRetrieveUpdateDestroyView,  # Generic view
    ProductViewSet       # ViewSet
)

router = DefaultRouter()
router.register(r'products-viewset', ProductViewSet, basename='product')

urlpatterns = [
    # Function-based view endpoints
    path('products/', product_list_create, name='product-list-create'),
    
    # Class-based view endpoint
    path('products/<int:pk>/class-update/', ProductUpdateView.as_view(), name='product-class-update'),
    
    # Generic view endpoints
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    
    # ViewSet endpoints (includes all CRUD operations)
    path('', include(router.urls)),
]