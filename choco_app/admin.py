from django.contrib import admin
from .models import FlavorSeason, Ingredient, CustomerSuggestion, AllergyIssue, Inquiry


@admin.register(FlavorSeason)
class FlavorSeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'available_from', 'available_to', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock')
    search_fields = ('name',)
    list_filter = ('stock',)


class AllergyIssueInline(admin.TabularInline):
    model = AllergyIssue
    extra = 1 

@admin.register(CustomerSuggestion)
class CustomerSuggestionAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'suggested_flavor')
    search_fields = ('customer_name', 'suggested_flavor')
    inlines = [AllergyIssueInline]

admin.site.register(Inquiry)
