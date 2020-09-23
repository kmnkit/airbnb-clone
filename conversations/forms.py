from django import forms


class AddCommentForm(forms.Form):
    message = forms.CharField(
        required=True, widget=forms.TextInput({"placeholder": "add a Comment."})
    )
