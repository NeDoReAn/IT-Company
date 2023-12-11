from django.contrib import admin

from .models import Customer, Developer, Tester, Database, Project


# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'phone_number')
    list_display_links = ('first_name', 'last_name', 'surname', 'phone_number')
    search_fields = ('first_name', 'last_name', 'surname', 'phone_number')


@admin.register(Developer)
class DeveloperModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'phone_number')
    list_display_links = ('first_name', 'last_name', 'surname', 'phone_number')
    search_fields = ('first_name', 'last_name', 'surname', 'phone_number')


@admin.register(Tester)
class TesterModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'surname', 'phone_number')
    list_display_links = ('first_name', 'last_name', 'surname', 'phone_number')
    search_fields = ('first_name', 'last_name', 'surname', 'phone_number')


@admin.register(Database)
class DatabaseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'admin')
    list_display_links = ('name', 'size', 'admin')
    search_fields = ('name', 'size', 'admin')


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'database')
    list_display_links = ('name', 'cost', 'database')
    search_fields = ('name', 'cost', 'database')
