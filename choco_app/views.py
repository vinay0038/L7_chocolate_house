from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingredient, FlavorSeason
from .forms import SuggestionForm, AllergyForm, InquiryForm, IngredientForm, SeasonalFlavorForm

def list_ingredients(request):
    """
    View to list all ingredients.

    This view retrieves all ingredients from the database and renders them
    in the 'ingredient.html' template.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the list of ingredients.
    """
    all_ingredients = Ingredient.objects.all()  
    return render(request, 'ingredient.html', {'ingredients': all_ingredients})

def create_customer_suggestion(request):
    """
    View to create a customer flavor suggestion.

    This view handles the form submission for customer suggestions.
    If the request method is POST and the form is valid, the suggestion is saved
    and the user is redirected to the success page. Otherwise, a blank form is displayed.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the suggestion form or a redirect
                      to the success page.
    """
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('suggestion_success')  
    else:
        form = SuggestionForm()

    return render(request, 'customer_suggestion.html', {'form': form})

def suggestion_success_view(request):
    """
    View to display the success page after a customer suggestion is created.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response for the suggestion success page.
    """
    return render(request, 'suggestion_success.html')

def view_seasonal_flavors(request):
    """
    View to list active seasonal flavors.

    This view retrieves all active flavors from the database and renders them
    in the 'season_flavor.html' template.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the list of active seasonal flavors.
    """
    active_flavors = FlavorSeason.objects.filter(is_active=True)  
    return render(request, 'season_flavor.html', {'flavors': active_flavors})

def create_allergy_concern(request):
    """
    View to create an allergy concern related to customer suggestions.

    This view handles the form submission for allergy concerns. If the request
    method is POST and the form is valid, the concern is saved and the user is
    redirected to the success page. Otherwise, a blank form is displayed.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the allergy concern form or a redirect
                      to the success page.
    """
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allergy_concern_success')  
    else:
        form = AllergyForm()
    
    return render(request, 'allergy_concern.html', {'form': form})

def allergy_concern_success_view(request):
    """
    View to display the success page after an allergy concern is created.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response for the allergy concern success page.
    """
    return render(request, 'allergy_sucess.html')

def home_view(request):
    """
    View for the home page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response for the home page.
    """
    return render(request, 'home.html')

def contact_view(request):
    """
    View for customer inquiries.

    This view handles the form submission for customer inquiries. If the request
    method is POST and the form is valid, the inquiry is saved and the user is
    redirected to the home page. Otherwise, a blank form is displayed.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the contact form or a redirect
                      to the home page.
    """
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})

def about_view(request):
    """
    View for the about page.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response for the about page.
    """
    return render(request, 'about.html')

def create_ingredient(request):
    """
    View to create a new ingredient.

    This view handles the form submission for creating a new ingredient. If the request
    method is POST and the form is valid, the ingredient is saved and the user is
    redirected to the ingredient list page. Otherwise, a blank form is displayed.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the ingredient creation form or a redirect
                      to the ingredient list page.
    """
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'ingredient_form.html', {'form': form})

def update_ingredient(request, pk):
    """
    View to update an existing ingredient.

    This view retrieves the ingredient by primary key and handles the form submission
    for updating its details. If the request method is POST and the form is valid,
    the ingredient is updated and the user is redirected to the ingredient list page.

    Parameters:
        request (HttpRequest): The request object.
        pk (int): The primary key of the ingredient to update.

    Returns:
        HttpResponse: Rendered HTML response with the ingredient update form or a redirect
                      to the ingredient list page.
    """
    ingredient_instance = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient_instance)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient_instance)
    return render(request, 'ingredient_form.html', {'form': form})

def delete_ingredient(request, pk):
    """
    View to delete an existing ingredient.

    This view retrieves the ingredient by primary key and confirms deletion. If the request
    method is POST, the ingredient is deleted and the user is redirected to the ingredient list page.

    Parameters:
        request (HttpRequest): The request object.
        pk (int): The primary key of the ingredient to delete.

    Returns:
        HttpResponse: Rendered HTML response for confirmation of deletion or a redirect
                      to the ingredient list page.
    """
    ingredient_instance = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient_instance.delete()
        return redirect('ingredient_list')
    return render(request, 'ingredient_delete.html', {'ingredient': ingredient_instance})

def add_seasonal_flavor(request):
    """
    View to add a new seasonal flavor.

    This view handles the form submission for creating a new seasonal flavor. If the request
    method is POST and the form is valid, the flavor is saved and the user is redirected
    to the seasonal flavor list page. Otherwise, a blank form is displayed.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the seasonal flavor creation form or a redirect
                      to the seasonal flavor list page.
    """
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seasonal_flavors')  
    else:
        form = SeasonalFlavorForm()
    return render(request, 'add_seasonal_flavor.html', {'form': form})

def update_seasonal_flavor(request, flavor_id):
    """
    View to update an existing seasonal flavor.

    This view retrieves the flavor by its ID and handles the form submission for updating
    its details. If the request method is POST and the form is valid, the flavor is updated
    and the user is redirected to the seasonal flavors page.

    Parameters:
        request (HttpRequest): The request object.
        flavor_id (int): The ID of the flavor to update.

    Returns:
        HttpResponse: Rendered HTML response with the seasonal flavor update form or a redirect
                      to the seasonal flavors page.
    """
    flavor = get_object_or_404(FlavorSeason, id=flavor_id)
    if request.method == 'POST':
        form = SeasonalFlavorForm(request.POST, instance=flavor)
        if form.is_valid():
            form.save()
            return redirect('seasonal_flavors')
    else:
        form = SeasonalFlavorForm(instance=flavor)
    return render(request, 'update_seasonal_flavour.html', {'form': form})

def delete_seasonal_flavor(request, flavor_id):
    """
    Delete an existing seasonal flavor.

    This view handles the deletion of a FlavorSeason object identified by its ID (flavor_id).
    If the request method is POST, it deletes the flavor and redirects to the seasonal flavor list.
    For GET requests, it renders a confirmation page to ensure the user intends to delete the flavor.

    Args:
        request: The HTTP request object.
        flavor_id (int): The ID of the flavor to be deleted.

    Returns:
        HttpResponse: 
            - On POST: Redirects to the seasonal flavor list.
            - On GET: Renders the confirmation template 'confirm_delete.html' with the flavor object.
    """
    flavor = get_object_or_404(FlavorSeason, id=flavor_id)  
    if request.method == 'POST':
        flavor.delete()  
        return redirect('seasonal_flavors') 
    return render(request, 'confirm_delete.html', {'flavor': flavor})  

