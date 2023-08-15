from rest_framework import serializers
from django.contrib.auth.models import User
from .models import GroceryList, GroceryItem

class GroceryItemSerializer(serializers.ModelSerializer):
    '''
    Serializer for Grocery Items.
    Converts GroceryItem model instances to JSON.
    '''
    class Meta:
        model = GroceryItem
        fields = '__all__'

class GroceryListSerializer(serializers.ModelSerializer):
    '''
    Serializer for Grocery Lists.
    Converts GroceryList model instances to JSON.
    '''
    # Including GroceryItemSerializer for nested representation of items.
    items = GroceryItemSerializer(many=True, read_only=True)

    class Meta:
        model = GroceryList
        fields = '__all__'
