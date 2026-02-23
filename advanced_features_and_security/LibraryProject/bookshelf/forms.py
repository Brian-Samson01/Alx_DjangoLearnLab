from django import forms


class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name"
    )


class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="Book Title"
    )