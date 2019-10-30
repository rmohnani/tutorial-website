from django.shortcuts import render
from tutoring.models import Tutor, Tutee

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tutors = Tutor.objects.all().count()
    num_tutees = Tutee.objects.all().count()
    
    context = {
        'num_tutors': num_tutors,
        'num_tutees': num_tutees,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def tutorsignup(request):
    custom_text = 'This is a custom text string'
    
    context = {
        'custom_text': custom_text,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tutorsignup.html', context=context)

def tuteesignup(request):
    custom_text = 'This is another custom text string'
    
    context = {
        'custom_text': custom_text,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'tuteesignup.html', context=context)