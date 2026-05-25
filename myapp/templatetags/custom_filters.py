from django import template

register = template.Library()

@register.filter
def currency(value):
  return f"${value}"

@register.filter
def discount(value,percent):
  return value-((value*percent)/100)