from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm, WishlistItemForm, WishlistTitleForm
from .models import Wishlist, WishlistItem


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_wishlist')
    else:
        form = SignUpForm()
    return render(request, 'wishlist/signup.html', {'form': form})


@login_required
def my_wishlist(request):
    wishlist, _created = Wishlist.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'update_title' in request.POST:
            title_form = WishlistTitleForm(request.POST, instance=wishlist)
            if title_form.is_valid():
                title_form.save()
            return redirect('my_wishlist')

        item_form = WishlistItemForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.wishlist = wishlist
            item.save()
            return redirect('my_wishlist')
    else:
        item_form = WishlistItemForm()

    title_form = WishlistTitleForm(instance=wishlist)

    share_url = request.build_absolute_uri(
        f'/wishlist/shared/{wishlist.share_token}/'
    )

    return render(request, 'wishlist/my_wishlist.html', {
        'wishlist': wishlist,
        'items': wishlist.items.all(),
        'title_form': title_form,
        'item_form': item_form,
        'share_url': share_url,
    })


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id, wishlist__user=request.user)
    if request.method == 'POST':
        item.delete()
    return redirect('my_wishlist')


def shared_wishlist(request, token):
    wishlist = get_object_or_404(Wishlist, share_token=token)
    return render(request, 'wishlist/shared_wishlist.html', {
        'wishlist': wishlist,
        'items': wishlist.items.all(),
    })
