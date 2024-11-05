from django import forms
from .models import CustomerSuggestion, Ingredient, AllergyIssue, Inquiry, FlavorSeason

class SuggestionForm(forms.ModelForm):
    """
    A form for submitting customer flavor suggestions.

    This form is based on the CustomerSuggestion model and includes fields for the customer's name,
    email, suggested flavor, reason for the suggestion, and any ingredients associated with the suggestion.

    Attributes:
        Meta (class): Contains metadata for the form including the model and fields to include.
    """
    class Meta:
        model = CustomerSuggestion  
        fields = ['customer_name', 'customer_email', 'suggested_flavor', 'suggestion_reason', 'ingredients']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),  # Display ingredients as checkboxes
        }


class AllergyForm(forms.ModelForm):
    """
    A form for submitting allergy issues related to customer suggestions.

    This form is based on the AllergyIssue model and includes fields for selecting the customer suggestion,
    the ingredient causing the allergy issue, and details about the allergy concern.

    Attributes:
        Meta (class): Contains metadata for the form including the model and fields to include.
    """
    class Meta:
        model = AllergyIssue 
        fields = ['customer_suggestion', 'ingredient', 'concern_detail']
        widgets = {
            'customer_suggestion': forms.Select(),  # Dropdown for selecting customer suggestions
            'ingredient': forms.Select(),  # Dropdown for selecting ingredients
        }


class InquiryForm(forms.ModelForm):
    """
    A form for customer inquiries.

    This form is based on the Inquiry model and includes fields for the customer's name, email address,
    and the content of their message.

    Attributes:
        Meta (class): Contains metadata for the form including the model and fields to include.
    """
    class Meta:
        model = Inquiry  
        fields = ['name', 'email', 'message']


class IngredientForm(forms.ModelForm):
    """
    A form for creating or updating ingredients.

    This form is based on the Ingredient model and includes fields for the ingredient's name and stock quantity.

    Attributes:
        Meta (class): Contains metadata for the form including the model and fields to include.
    """
    class Meta:
        model = Ingredient  
        fields = ['name', 'stock']


class SeasonalFlavorForm(forms.ModelForm):
    """
    A form for creating or updating seasonal flavors.

    This form is based on the FlavorSeason model and includes fields for the flavor's name, description,
    availability dates, and whether the flavor is active.

    Attributes:
        Meta (class): Contains metadata for the form including the model and fields to include.
    """
    class Meta:
        model = FlavorSeason
        fields = ['name', 'description', 'available_from', 'available_to', 'is_active']
