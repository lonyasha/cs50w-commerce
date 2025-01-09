from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=100)
    start_bid = models.IntegerField()
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    creator = models.ForeignKey('User', on_delete=models.CASCADE, related_name='listings')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='listings', blank=True, null=True)
    winning_bid = models.ForeignKey('Bid', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='won_auctions')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.creator.username}"


class Bid(models.Model):
    offer = models.IntegerField()
    bidder = models.ForeignKey('User', on_delete=models.CASCADE, related_name='bids')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='bids')

    def __str__(self):
        return f"${self.offer} on {self.listing.title} by {self.bidder.username}"


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='comments')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.user.username} on {self.listing.title}"


class Watchlist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='watchlist')
    listings = models.ManyToManyField(Listing)

    def __str__(self):
        return f"{self.user.username}'s Watchlist"