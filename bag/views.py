from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))  # got quantity from input
    redirect_url = request.POST.get('redirect_url')  # after item is added to bag redirect user to the same page
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):  # cjeck if element exists
        bag[item_id] += quantity  # update quantity
    else:
        bag[item_id] = quantity  # create and add quantity to cart

    request.session['bag'] = bag
    return redirect(redirect_url)
