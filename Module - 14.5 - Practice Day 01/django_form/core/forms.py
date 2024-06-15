from django import forms
from django.forms.widgets import DateInput
import datetime
from django.core import validators


class Info_Form(forms.Form):
    name = forms.CharField(
        max_length=50,
        initial="Jabed Hosen",
        label="Your Name",
        help_text="Enter your name maximum 50 charecters",
    )
    about = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(attrs={"rows": 4}),
        label="Write about yourself",
        help_text="Maximum 200 charecters",
    )
    email = forms.EmailField(label="Enter your email", help_text=".com is required")
    dob = forms.DateField(widget=DateInput(attrs={"type": "date"}), label="DOB")
    BIRTH_YEAR_CHOICES = ["Year", 2000, 2001, 2002, 2003, 2004, 2005]
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )

    height = forms.DecimalField(label="Your height")
    weight = forms.DecimalField(label="Your weight")

    FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("yellow", "Yellow"),
        ("black", "Black"),
        ("white", "White"),
    ]

    favorite_color = forms.ChoiceField(
        choices=FAVORITE_COLORS_CHOICES, widget=forms.RadioSelect
    )

    submission_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), initial=datetime.date.today
    )

    agree = forms.BooleanField(label="agree with this terms & conditions.")


class Doc_Form(forms.Form):
    name = forms.CharField(
        max_length=50,
        initial="Jabed Hosen",
        label="Your Name",
        help_text="Enter your name, maximum 50 characters",
    )
    file = forms.FileField(
        help_text="Please provide your file (pdf or docx)*",
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["pdf", "docx"],
                message="Only .pdf and .docx files are allowed",
            )
        ],
    )
    profile_image = forms.ImageField(
        help_text="Please provide a (png or jpg)* image",
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=["png", "jpg"],
                message="Only .png and .jpg images are allowed",
            )
        ],
    )
   
