# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

from django import forms


class AddPlantForm(forms.Form):
    plant_name = forms.CharField(
        label="Plant name",
        max_length=100,
    )
    plant_description = forms.CharField(label="Plant description", widget=forms.Textarea(attrs={"rows": "5"}))
