"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from . import script

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def signup(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup.html',
        {
            'title': 'Sign Up',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def form(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        print('post')
        revenue = request.POST.get("revenue_field")
        date = request.POST.get("date_field")
        hours = request.POST.get("hours_field")
        salary = request.POST.get("salary_field")
        cost = request.POST.get("cost_field")
        units = request.POST.get("units_field")

    print(date)

    return render(
        request,
        'app/form.html',
        {
            'title': 'Form',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def financialhealth(request):
    return render(
        request,
        "app/financialhealth.html",
        {
            'labels': ['F', 'M'],
            'data': [52, 82],
            'colors': ["#FF4136", "#0074D9"]
        }
    )
