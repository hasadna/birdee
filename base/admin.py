from .forms.models import BlameBaseFormSet


class BlameBaseAdmin(object):
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class BlameBaseFormsetAdmin(object):
    """
    Use a generic formset which populates the 'user_field' model field
    with the currently logged in user.
    """
    formset = BlameBaseFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.request = request
        return formset


class BlameBaseAdminMixin(BlameBaseAdmin, BlameBaseFormsetAdmin):
    pass
