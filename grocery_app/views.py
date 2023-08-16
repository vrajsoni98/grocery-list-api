from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import GroceryList, GroceryItem
from .serializers import GroceryListSerializer, GroceryItemSerializer

class GroceryListList(generics.ListCreateAPIView):
    '''
    API view to list and create grocery lists.
    Lists all existing grocery lists or creates a new one.
    '''
    serializer_class = GroceryListSerializer

    def get_queryset(self):
        return GroceryList.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class GroceryListDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view to retrieve, update, and delete a specific grocery list.
    Retrieves, updates, or deletes the details of a grocery list.
    '''
    serializer_class = GroceryListSerializer

    def get_queryset(self):
        return GroceryList.objects.all()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class GroceryItemList(generics.ListCreateAPIView):
    '''
    API view to list and create grocery items for a specific list.
    Lists all existing grocery items or creates a new one within a list.
    '''
    serializer_class = GroceryItemSerializer
        
    def get_queryset(self):
        list_id = self.kwargs['list_id']
        # Get the specific grocery list using the list_id
        grocery_list = get_object_or_404(GroceryList, id=list_id)
        # Filter the related grocery items for the specific grocery list
        return GroceryItem.objects.filter(grocery_list=grocery_list)

    def perform_create(self, serializer):
        list_id = self.kwargs['list_id']
        # Get the specific grocery list using the list_id
        grocery_list = get_object_or_404(GroceryList, id=list_id)
        serializer.save(grocery_list=grocery_list)

class GroceryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view to retrieve, update, and delete a specific grocery item within a list.
    Retrieves, updates, or deletes the details of a grocery item within a list.
    '''
    serializer_class = GroceryItemSerializer

    def get_queryset(self):
        list_id = self.kwargs['list_id']
        # Get the specific grocery list using the list_id
        grocery_list = get_object_or_404(GroceryList, id=list_id)
        # Filter the related grocery items for the specific grocery list
        return GroceryItem.objects.filter(grocery_list=grocery_list)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
