# capapp/templatetags/str_extensions.py
from django import template

register = template.Library()

def capitalize_first_letter(value):
    return value.capitalize()

def superoutput(inputstr):
    #result = []
    #letter = inputstr
    #letter = letter.upper()
    #result.append(letter)
    #return ''.join(result)
    return inputstr.upper()


register.filter('capitalize_first_letter', capitalize_first_letter)
register.filter('superoutput', superoutput)
