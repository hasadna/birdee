from django.forms.models import BaseInlineFormSet


class BlameBaseFormSet(BaseInlineFormSet):
    """
    This is intended to be used with base.admin.BlameBaseFormsetAdmin so self.request is set
    """
    def save_new(self, form, commit=True):
        """
        :param django.forms.Form form:
        :param bool commit:
        :rtype: django.db.models.Model
        """
        obj = super().save_new(form, commit=False)
        obj.created_by = self.request.user
        obj.updated_by = self.request.user
        if commit:
            obj.save()
        return obj

    def save_existing(self, form, instance, commit=True):
        """
        :param django.forms.Form form:
        :param bool commit:
        :rtype: django.db.models.Model
        """
        obj = super().save_existing(form, instance, commit=False)
        obj.updated_by = self.request.user
        if commit:
            obj.save()
        return obj
