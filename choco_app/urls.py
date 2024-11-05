from django.urls import path
from .views import list_ingredients, create_customer_suggestion,suggestion_success_view, view_seasonal_flavors, create_allergy_concern, allergy_concern_success_view,home_view,contact_view, about_view,create_ingredient, update_ingredient, delete_ingredient, add_seasonal_flavor, update_seasonal_flavor,delete_seasonal_flavor

urlpatterns = [
    path('ingredients/', list_ingredients, name='ingredient_list'),
    path('ingredients/create/', create_ingredient, name='ingredient_create'),
    path('ingredients/update/<int:pk>/',update_ingredient, name='ingredient_update'),
    path('ingredients/delete/<int:pk>/', delete_ingredient, name='ingredient_delete'),
    path('suggest/', create_customer_suggestion, name='customer_suggestion'),
    path('suggest/success/', suggestion_success_view, name='suggestion_success'),
    path('seasonal_flavors/', view_seasonal_flavors, name='seasonal_flavors'),
    path('allergy_concern/', create_allergy_concern, name='allergy_concern_create'),
    path('allergy_concern/success/', allergy_concern_success_view, name='allergy_concern_success'),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),  
    path('about/', about_view, name='about'),
    path('seasonal_flavors/add/', add_seasonal_flavor, name='add_seasonal_flavor'),
    path('seasonal_flavors/<int:flavor_id>/update/', update_seasonal_flavor, name='update_seasonal_flavor'),
    path('seasonal_flavors/<int:flavor_id>/delete/', delete_seasonal_flavor, name='delete_seasonal_flavor'),

]
