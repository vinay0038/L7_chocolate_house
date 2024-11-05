# Chocolate House Web Application

## Overview

Welcome to the L7 Chocolate House web application! This application showcases our variety of seasonal chocolate flavors, emphasizing quality ingredients and sustainable practices. Built using Django, it provides an engaging user experience for chocolate lovers.

## Features

- **Seasonal Chocolate Flavors**: Explore a selection of delicious seasonal flavors.
- **Quality Ingredients**: Learn about our commitment to using locally sourced ingredients.
- **Responsive Design**: The web app is designed to be fully responsive and accessible on all devices.
- **User-Friendly Interface**: Simple navigation to enhance user experience.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (or any preferred database)
- **Static Files**: Managed using Django's static files framework

## Installation

Follow these steps to set up the Chocolate House web application on your local machine:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chocolate-house

2. **Create a virtual environment:**

   ```bash
   python -m venv env

3. **Activate the virtual environment:**

   **On Windows:**
     ```bash  
    env\Scripts\activate
   
    **On macOS/Linux:**
    
    source env/bin/activate


4. **Run database migrations:**

  ```bash

    python manage.py migrate
    
5. **Start the development server:**

  ```bash

python manage.py runserver


6. **Access the application: Open your web browser and go to:**

  ```bash
http://127.0.0.1:8000/inventory



## Test Cases Documentation

**Test Case 1:**List Ingredients
 **Test Case ID:** TC001

 **Description**: Verify that the ingredients list page displays all available ingredients.

 **Preconditions**: At least one ingredient must exist in the database.

 **Steps:**
    Navigate to the ingredients list page at http://127.0.0.1:8000/ingredients/.

  **Expected Result:** The page should load successfully and display a list of all ingredients.


**Test Case 2:** Create Ingredient

**Test Case ID:** TC002

**Description**: Verify that a new ingredient can be created.

**Preconditions**: none

**Steps:**
    Navigate to the create ingredient page at http://127.0.0.1:8000/ingredients/create/.
    Fill in the ingredient form with valid data.
    Submit the form.

**Expected Result**: The ingredient should be created successfully, and the user should be redirected to the ingredient list page showing the new ingredient.


**Test Case 3:** Update Ingredient

**Test Case ID:** TC003

**Description**: Verify that an existing ingredient can be updated.

**Preconditions**: At least one ingredient must exist in the database.

**Steps:**

    Navigate to the ingredient update page for an existing ingredient at http://127.0.0.1:8000/ingredients/update/<ingredient_id>/.
    Modify the ingredient details.
    Submit the form.

**Expected Result**: The ingredient should be updated successfully, and the updated details should reflect on the ingredient list page.


**Test Case 4:** Delete Ingredient

**Test Case ID:** TC004

**Description:** Verify that an ingredient can be deleted.

**Preconditions:** At least one ingredient must exist in the database.

**Steps:**
    Navigate to the ingredient delete page for an existing ingredient at http://127.0.0.1:8000/ingredients/delete/<ingredient_id>/.
    Confirm the deletion.
    Expected Result: The ingredient should be deleted successfully, and the ingredient list page should no longer display the deleted ingredient.


**Test Case 5:** Customer Suggestion

**Test Case ID:** TC005

**Description**: Verify that a customer can submit a suggestion.

**Preconditions:** User is on the suggestion page.

**Steps:**
    Navigate to the suggestion page at http://127.0.0.1:8000/suggest/.
    Fill out the suggestion form with valid data.
    Submit the form.

**Expected Result:** The suggestion should be saved, and the user should be redirected to the success page.


**Test Case 6**: View Seasonal Flavors

**Test Case ID:** TC006

**Description:** Verify that the seasonal flavors page displays all seasonal chocolate flavors.

**Preconditions:** At least one seasonal flavor must exist in the database.

**Steps:**
    Navigate to the seasonal flavors page at http://127.0.0.1:8000/seasonal_flavors/.
    Expected Result: The page should load successfully and display a list of all seasonal chocolate flavors.


**Test Case 7**: Create Allergy Concern

**Test Case ID**: TC007

**Description**: Verify that a user can submit an allergy concern.

**Preconditions:** User is on the allergy concern page.

**Steps:**
    Navigate to the allergy concern page at http://127.0.0.1:8000/allergy_concern/.
    Fill out the allergy concern form with valid data.
    Submit the form.

**Expected Result**: The allergy concern should be saved, and the user should be redirected to the success page.


**Test Case 8**: Contact Page

**Test Case ID**: TC008

**Description**: Verify that the contact page loads successfully.

**Preconditions**: None.

**Steps**:
    Navigate to the contact page at http://127.0.0.1:8000/contact/.

**Expected Result**: The contact page should load successfully without errors.


**Test Case 9**: About Page

**Test Case ID**: TC009

**Description**: Verify that the about page loads successfully.

**Preconditions**: None.

**Steps**:
    Navigate to the about page at http://127.0.0.1:8000/about/.

**Expected Result**: The about page should load successfully without errors.



## SQL Query or ORM Abstraction Implementation

The Chocolate House web application utilizes Django's Object-Relational Mapping (ORM) system for seamless interaction with the database. Below are the key models used in the application:

### Models

#### FlavorSeason
Represents a seasonal flavor with details on availability and status.
```python
class FlavorSeason(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    available_from = models.DateField()
    available_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


#### Ingredient
Represents an ingredient used in various flavors, along with its stock information.


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    stock = models.FloatField(help_text="grams or units")

    def __str__(self):
        return self.name


### CustomerSuggestion
Captures customer flavor suggestions, including their contact information and associated ingredients.


class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    suggested_flavor = models.CharField(max_length=100)
    suggestion_reason = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='suggestions', blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.suggested_flavor}"


### AllergyIssue
Represents allergy concerns associated with a specific customer suggestion.


class AllergyIssue(models.Model):
    customer_suggestion = models.ForeignKey(CustomerSuggestion, related_name="allergy_issues", on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, related_name="allergy_problems", on_delete=models.CASCADE)
    concern_detail = models.TextField(help_text="Details about the allergy concern")

    def __str__(self):
        return f"Allergy Issue: {self.customer_suggestion.customer_name} - {self.ingredient.name}"


### Inquiry
Handles inquiries from customers regarding the products or services.


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.email}"


####Query Examples
Here are examples of how to perform common database operations using the Django ORM:

###Retrieve All Ingredients

ingredients = Ingredient.objects.all()

###Create a New Customer Suggestion

new_suggestion = CustomerSuggestion.objects.create(
    customer_name='Vinay M',
    customer_email='vinayvini0038@gmail.com',
    suggested_flavor='Chocolate Mint',
    suggestion_reason='Love the combination of chocolate and mint!'
)

###Add an Allergy Issue

allergy_issue = AllergyIssue.objects.create(
    customer_suggestion=new_suggestion,
    ingredient=Ingredient.objects.get(name='Nuts'),
    concern_detail='Customer has a nut allergy.'
)


###Filter Seasonal Flavors

active_flavors = FlavorSeason.objects.filter(is_active=True)

# Docker Implementation for Chocolate House App

This section describes how to set up and run the Chocolate House Django application using Docker.

## Prerequisites

- Ensure you have [Docker](https://www.docker.com/get-started) installed on your machine.

## Directory Structure

When you clone the repository, you will find the following structure:

## Build the Docker Image

1. Open your terminal and navigate to the `chocolate_house` directory:

   ```bash
   cd chocolate_house

2.Build the Docker image by running the following command:

  docker build -t chocolate_app .

3.Run the Docker Container
   
   docker run -p 8000:8000 chocolate_app

4.Stopping the Container
   
   docker ps

   Then stop the container using:
   
   docker stop <container_id>