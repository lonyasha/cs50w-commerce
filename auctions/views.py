from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import User, Listing, Category, Watchlist
from .forms import ListingForm, BidForm, CommentForm


def index(request):
    listings = Listing.objects.filter(active=True).order_by('title')
    return render(request, "auctions/index.html", {'listings': listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    in_watchlist = False
    local_watchlist = None
    user_is_winner = False

    if not listing.active and listing.winning_bid:
        if listing.winning_bid.bidder == request.user:
            user_is_winner = True

    if request.user.is_authenticated:
        local_watchlist, created = Watchlist.objects.get_or_create(user=request.user)
        in_watchlist = listing in local_watchlist.listings.all()

    if request.user.is_authenticated and request.method == 'POST':
        if 'close_auction' in request.POST:
            highest_bid = listing.bids.order_by('-offer').first()
            listing.winning_bid = highest_bid
            listing.active = False
            listing.save()
            return redirect('listing', pk=pk)
        elif 'add_to_watchlist' in request.POST:
            local_watchlist.listings.add(listing)
            return redirect('listing', pk=pk)
        elif 'remove_from_watchlist' in request.POST:
            local_watchlist.listings.remove(listing)
            return redirect('listing', pk=pk)
        elif 'place_bid' in request.POST:
            bid_form = BidForm(request.POST)
            if bid_form.is_valid():
                new_bid = bid_form.cleaned_data['offer']
                current_highest_bid = listing.bids.order_by('-offer').first()
                if current_highest_bid is None or new_bid > current_highest_bid.offer:
                    if new_bid >= listing.start_bid:
                        bid = bid_form.save(commit=False)
                        bid.listing = listing
                        bid.bidder = request.user
                        bid.save()
                        messages.success(request, 'Your bid was successfully placed!')
                        return redirect('listing', pk=pk)
                    else:
                        messages.error(request, 'Your bid must be at least as high as the starting bid.')
                else:
                    messages.error(request, f'Your bid must be higher than the current highest bid - ${current_highest_bid.offer}.')
            else:
                messages.error(request, 'There was an error with your bid submission.')
        elif 'add_comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.listing = listing
                comment.user = request.user
                comment.save()
                return redirect('listing', pk=pk)

    bid_form = BidForm()
    comment_form = CommentForm()
    return render(request, 'auctions/listing_detail.html',
                  {'listing': listing, 'bid_form': bid_form, 'comment_form': comment_form,
                   'in_watchlist': in_watchlist, 'user_is_creator': request.user == listing.creator,
                   'user_is_winner': user_is_winner, })


@login_required
def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.creator = request.user
            listing.active = True
            listing.save()
            return redirect('index')
    else:
        form = ListingForm()
    return render(request, 'auctions/create_listing.html', {'form': form})


def categories(request):
    return render(request, 'auctions/categories.html')


def category_listings(request, category_id):
    category = Category.objects.get(id=category_id)
    listings = category.listings.filter(active=True).order_by('title')
    return render(request, 'auctions/category_listings.html', {'listings': listings, 'category': category})


@login_required
def watchlist(request):
    local_watchlist = request.user.watchlist.all()
    listings = Listing.objects.filter(watchlist__in=local_watchlist).order_by('title')
    return render(request, 'auctions/watchlist.html', {'listings': listings})
