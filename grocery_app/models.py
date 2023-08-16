from django.db import models

class GroceryList(models.Model):
    '''
    Model for Grocery Lists.
    Users can create multiple grocery lists.
    '''
    
    # Name of the grocery list.
    name = models.CharField(max_length=255)
    # Short description of the list.
    description = models.CharField(max_length=255, null=True)
    # Date and time of list creation.
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroceryItem(models.Model):
    '''
    Model for Grocery List Items.
    Users can create multiple grocery list items.
    '''
    
    # Name of the grocery item.
    name = models.CharField(max_length=255)
    # Quantity of the item required.
    quantity = models.PositiveIntegerField(default=1)
    # Boolean indicating whether the item is purchased or not.
    purchased = models.BooleanField(default=False)
    # Relation to the corresponding grocery list.
    grocery_list = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
