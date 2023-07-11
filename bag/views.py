from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return bag contents page """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of specified product to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')