# Generated by Django 4.2.4 on 2023-08-14 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_app', '0002_remove_grocerylist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='groceryitem',
            name='description',
        ),
        migrations.RemoveField(
            model_name='groceryitem',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='grocerylist',
            name='updated_on',
        ),
    ]
