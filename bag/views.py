from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return bag contents page """
    
    return render(request, 'bag/bag.html')