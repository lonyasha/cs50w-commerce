from django import forms
from .models import Listing, Bid, Comment


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'start_bid', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-4'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_bid': forms.NumberInput(attrs={'class': 'form-control col-auto'}),
            'category': forms.Select(attrs={'class': 'form-control col-auto'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'image URL'}),
        }


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['offer']
        widgets = {
            'offer': forms.NumberInput(attrs={'class': 'form-control bid-input'}),
        }
        labels = {
            'offer': 'Place a bid',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Your comment', 'style': 'height: 60px'}),
        }
        labels = {
            'text': '',
        }
