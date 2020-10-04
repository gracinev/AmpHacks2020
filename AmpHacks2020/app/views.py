"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse

from .models import PredResults

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
    form_class = DataForm()
    dataform = DataForm()
    return render(request, 'app/form.html', {'form': dataform, })


def analyze_form(request):
    if request.POST.get('action') == 'post':
        Revenue = float(request.POST.get('Revenue'))
        Cost = float(request.POST.get('Cost'))
        Lease = float(request.POST.get('Lease'))
        Product = float(request.POST.get('Product'))
        Utilities = float(request.POST.get('Utilities'))
        Assets = float(request.POST.get('Assets'))

        #path to model here
        model = pd.read_pickle()

        # variables from fields put through the model
        result = model.predict([[Revenue, Cost, Lease, Utilities, Product, Assets]])

        analyzedResult = result[0]

        return JsonResponse({'result': analyzedResult, "Revenue": Revenue, "Cost": Cost, "Lease": Lease, "Utilities": Utilities, "Product": Product, "Assets": Assets}, safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)