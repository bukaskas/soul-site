from django import forms
from .models import Booking,Service, Staff, Customer
from datetime import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q



GENDER_CHOICES = [
    ('MR', 'Male'),
    ('MRS', 'Female'),
    
]

class DateInput(forms.DateInput):
    input_type = 'date'

class TextInput(forms.TextInput):
    input_type= 'text'




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

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name'
        }
        
class StaffForm(forms.Form):
    type = forms.CharField()
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
class SessionForm(forms.Form):
    HOURS = [
        ('0',0),
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5),
    ]

    MINUTES = [
        ('0',0),
        ('15',15),
        ('30',30),
        ('45',45),
    ]

    lesson = forms.ModelChoiceField(queryset=None,label="Type of Lesson")
    staff = forms.ModelChoiceField(queryset=Staff.objects.all(),label='Instructor')
    hours = forms.ChoiceField(choices=HOURS,label='Hours')
    minutes = forms.ChoiceField(choices=MINUTES,required=False,label='minutes')

    """ Select only course type of service """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Need to fix the filter for staff filter

        self.fields['lesson'].queryset = Service.objects.filter(category__icontains='course')
       
        