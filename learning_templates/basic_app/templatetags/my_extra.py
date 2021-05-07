from django import template

register = template.Library()

def cut_strg(value,arg):
    '''
    this cuts out value of 'arg' from the string..
    '''
    return value.replace(arg,'')

register.filter('cut_strg',cut_strg)

# WE CAN MAY REGISTER IT USING 'DECORATERS'
