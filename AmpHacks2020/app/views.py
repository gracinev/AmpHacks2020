"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
import pandas as pd
import math
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
        # print('post')
        revenue = int(request.POST.get("revenue_field"))
        date = request.POST.get("date_field")
        num_staff = int(request.POST.get("staff_field"))
        hours = int(request.POST.get("hours_field"))
        salary = int(request.POST.get("salary_field"))
        cost = int(request.POST.get("cost_field"))
        units = int(request.POST.get("units_field"))

        rev = script.predict_rev(revenue, pd.to_datetime(date))

        costs_fixed = script.fixed_costs(5000, "m", 12000, "y")
        costs_staff = script.staff_costs(num_staff, hours, salary)
        costs_product = script.product_costs(500, 2, cost, units)

        # print("Fixed Costs:", costs_fixed, "Staff Costs:", costs_staff, "Product Costs:", costs_product)

        profit = math.ceil(script.profit(rev, costs_fixed['daily_rent'] + costs_fixed['daily_util'] + costs_staff + costs_product))

        if profit < 0:
            days_left = math.ceil(5000/abs(profit))
            return render(
                request,
                'app/results.html',
                {
                    
                    'title': 'Financial Health',
                    'status': 'Projected daily loss:',
                    'profit': '${}'.format(abs(profit)),
                    'message': 'You are projected to make a loss. At current rates, your business can only operate for {} more days.'.format(days_left),
                    'recommendation': '',
                    'labels': ['12/4/2016', '12/5/2016', '12/5/2016', '12/7/2016', '12/8/2016', '12/9/2016',
                               '12/10/2016', '12/11/2016', '12/12/2016', '12/13/2016'],
                    'data': [1151.1151, 1117.4534, 1117.4534, 1161.706138, 1210.953996, 1185.783088, 1131.525112,
                             1122.15256, 1522.685036, 1269.59994],
                }
            )

        return render(
            request,
            'app/form.html',
            {
                'title': 'Financial Health',
                'status': 'Projected daily profit:',
                'profit': '${}'.format(abs(profit)),
                'message': 'You are projected to continue making profits.'
            }
        )

    else:
        return render(request, 'app/form.html', {})


def financialhealth(request):
    return render(
        request,
        "app/financialhealth.html",
        {
            
            'title': 'Financial Health',
            'labels': ['12/4/2016', '12/5/2016', '12/5/2016', '12/7/2016', '12/8/2016', '12/9/2016', '12/10/2016', '12/11/2016', '12/12/2016', '12/13/2016'],
            'data': [1151.1151, 1117.4534, 1117.4534, 1161.706138, 1210.953996, 1185.783088, 1131.525112, 1122.15256, 1522.685036, 1269.59994],
        }
    )
