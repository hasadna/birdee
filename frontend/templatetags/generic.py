from django import template

register = template.Library()


@register.assignment_tag
def is_self(object_user, request_user):
    return object_user == request_user
