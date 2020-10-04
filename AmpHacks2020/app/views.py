"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from .forms import DataForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def signup(request):
    """Renders the sign up page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/signup.html',
        {
            'title':'Sign Up',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def form(request):
    assert isinstance(request, HttpRequest)
    Revenue = request.POST.get('Revenue')
    Cost = request.POST.get('Cost')
    Lease = request.POST.get('Lease')
    Product = request.POST.get('Product')
    Assets = request.POST.get('Assets')
    Utilities = request.POST.get('Utilities')
    form_class = DataForm()
    dataform = DataForm()
    return render(request, 'app/form.html', {'form': dataform, 'Revenue': Revenue, 'Cost': Cost,
                                             'Lease': Lease, 'Product': Product, 'Assets': Assets,
                                             'Utilities': Utilities, })
