from django.forms.models import ModelForm
from django.forms import DateInput as BaseDateInput


class BlameBaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('account')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.instance.id:
            self.instance.created_by = self.user
        self.instance.updated_by = self.user
        return super().save(commit)


class DateInput(BaseDateInput):
    input_type = 'date'

