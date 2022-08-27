from django import template

register = template.Library()

# Returns the value of the a dictionary given it's key
@register.filter(name="key")
def get_value_from_key(dictionary, key):
    return dictionary.get(key)