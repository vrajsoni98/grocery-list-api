from django.urls import path
from .views import (
    GroceryListList,
    GroceryListDetail,
    GroceryItemList,
    GroceryItemDetail,
    # UserRegistrationView,
    # CustomAuthToken,
)

urlpatterns = [
    # Grocery List URLs
    path('grocerylists/', GroceryListList.as_view(), name='grocerylist-list'),
    path('grocerylists/<int:pk>/', GroceryListDetail.as_view(), name='grocerylist-detail'),
    
    # URL for listing and creating grocery items within a specific grocery list
    path('grocerylists/<int:list_id>/groceryitems/', GroceryItemList.as_view(), name='groceryitem-list-for-list'),

    # URL for viewing, updating, and deleting a specific grocery item within a specific grocery list
    path('grocerylists/<int:list_id>/groceryitems/<int:pk>/', GroceryItemDetail.as_view(), name='groceryitem-detail-for-list'),
] 