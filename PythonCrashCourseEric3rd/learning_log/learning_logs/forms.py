from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # Create a form based on this model
        fields = ['text'] # Use only the text field
        labels = {'text': ''} # Tells to not generate a label for this text

# We will redirect user to the new_topic page