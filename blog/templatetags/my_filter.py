from django.template import Library


register = Library()

@register.filter(name='displayName')
def displayName(value, arg):
    return eval('value.get_'+arg+'_display()')#eval字符串方法了解一下


    