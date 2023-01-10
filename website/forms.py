from django import forms
from .models import Booking
from datetime import datetime
from django.forms import ModelForm


GENDER_CHOICES = [
    ('MR', 'Male'),
    ('MRS', 'Female'),
    
]

class DateInput(forms.DateInput):
    input_type = 'date'

class TextInput(forms.TextInput):
    input_type= 'text'


# class BookingForm(forms.Form):
#     booking_date = forms.DateField(label="Booking date",widget=DateInput)
#     customer_name = forms.CharField(label="First Name")
#     customer_fname = forms.CharField(label="Family Name")

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields ="__all__"
        today = datetime.now()
        today_string = today.strftime("%Y-%m-%d")
        widgets = {
            'date':DateInput(attrs={'min':today_string,
                                    'class':'form-control'}),
            'customer_name':TextInput(attrs={'class':'form-control'}),
            'customer_fname':TextInput(attrs={'class':'form-control'}),
            'contact_number':TextInput(attrs={'class':'form-control'}),
            'nop':TextInput(attrs={'class':'form-control'}),
            
            }
        labels = {
            "nop":"Number of guests",
            "date":"Choose date for booking",
            "customer_name":"First name",
            "customer_fname":"Family name"
        }
        
class CustomerForm(forms.Form):
    name=forms.CharField(label="Full name")
    phone_nr=forms.CharField(label="Phone number")
    email=forms.EmailField(label="Email address")
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    weight=forms.IntegerField(label="Weight")
    terms=forms.BooleanField(label='Check if you agree on terms in waiver form?', required=True)
    gender.widget.attrs.update({'class':'choice'})

class PaymentForm(forms.Form):
    visa=forms.IntegerField(label="Visa",required=False)
    cash=forms.IntegerField(label='Cash',required=False)
    other=forms.IntegerField(label='Other type',required=False)
    comment=forms.CharField(widget=forms.Textarea(attrs={'name':'comment','style':'height = 3.2rem','label':'Comment'}),required=False)


