from django import forms
from django.contrib.auth.models import User
from pizzaplace.models import CartItem


class AddToCartForm(forms.Form):
    item_type = forms.CharField()
    item_id = forms.IntegerField()
    quantity = forms.IntegerField()

    def create_items_from_form(self, user: User):
        if self.is_valid():
            item_type = self.cleaned_data['item_type']
            item_id = self.cleaned_data['item_id']
            quantity = self.cleaned_data['quantity']
            CartItem.objects.create(item_type=item_type, item_id=item_id, quantity=quantity, cart=user.cart)
