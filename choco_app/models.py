from django.db import models

class FlavorSeason(models.Model):
    """
    Represents a seasonal chocolate flavor available in the Chocolate House.
    
    Attributes:
        name (str): The name of the flavor.
        description (str): A description of the flavor (optional).
        available_from (date): The date from which the flavor is available.
        available_to (date): The date until which the flavor is available.
        is_active (bool): Indicates whether the flavor is currently active.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    available_from = models.DateField()
    available_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return the name of the flavor."""
        return self.name


class Ingredient(models.Model):
    """
    Represents an ingredient used in chocolate flavors.
    
    Attributes:
        name (str): The name of the ingredient.
        stock (float): The quantity of the ingredient available in grams or units.
    """
    name = models.CharField(max_length=100, unique=True)
    stock = models.FloatField(help_text="grams or units")
    
    def __str__(self):
        """Return the name of the ingredient."""
        return self.name


class CustomerSuggestion(models.Model):
    """
    Captures customer suggestions for new chocolate flavors.
    
    Attributes:
        customer_name (str): The name of the customer.
        customer_email (str): The email address of the customer.
        suggested_flavor (str): The suggested flavor by the customer.
        suggestion_reason (str): The reason for the suggestion (optional).
        ingredients (ManyToManyField): Ingredients related to the suggested flavor.
    """
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    suggested_flavor = models.CharField(max_length=100)
    suggestion_reason = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='suggestions', blank=True)

    def __str__(self):
        """Return a string representation of the suggestion."""
        return f"{self.customer_name} - {self.suggested_flavor}"


class AllergyIssue(models.Model):
    """
    Represents an allergy concern related to a customer suggestion.
    
    Attributes:
        customer_suggestion (ForeignKey): The related customer suggestion that the allergy issue is associated with.
        ingredient (ForeignKey): The ingredient that is causing the allergy issue.
        concern_detail (str): Details about the allergy concern.
    """
    customer_suggestion = models.ForeignKey(CustomerSuggestion, related_name="allergy_issues", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name="allergy_problems", on_delete=models.CASCADE)
    concern_detail = models.TextField(help_text="Details about the allergy concern")

    def __str__(self):
        """Return a string representation of the allergy issue."""
        return f"Allergy Issue: {self.customer_suggestion.customer_name} - {self.ingredient.name}"
    

class Inquiry(models.Model):
    """
    Represents an inquiry submitted by a customer.
    
    Attributes:
        name (str): The name of the person making the inquiry.
        email (str): The email address of the person making the inquiry.
        message (str): The content of the inquiry message.
        created_at (datetime): The timestamp when the inquiry was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the inquiry."""
        return f"Inquiry from {self.name} - {self.email}"
