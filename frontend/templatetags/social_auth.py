from django import template

register = template.Library()

social_buttons = {
    'github': {
        'btn': 'github',
        'fa': 'github',
        'title': 'Github',
    },
    'gitlab': {
        'btn': 'github',
        'fa': 'github',
        'title': 'Gitlab',
    },
    'facebook': {
        'btn': 'facebook',
        'fa': 'facebook',
        'title': 'Facebook',
    },
    'google-oauth2': {
        'btn': 'google',
        'fa': 'google',
        'title': 'Google',
    },
    'yahoo-oauth2': {
        'btn': 'yahoo',
        'fa': 'yahoo',
        'title': 'Yahoo',
    },
}


@register.assignment_tag()
def backend_buttons(backends):
    associated = []
    for network in backends['associated']:
        associated.append((network.provider, network, social_buttons.get(network.provider)))
    return {
        'associated': associated,
        'not_associated': sorted({b: social_buttons[b] for b in backends['not_associated'] if b in social_buttons}.items()),
        'backends': sorted({b: social_buttons[b] for b in backends['backends'] if b in social_buttons}.items()),
    }
