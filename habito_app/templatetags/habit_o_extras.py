from django import template

register = template.Library()

# Inlude bootstrap
@register.simple_tag
def bootstrap():
	bootstrap_string='<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>'
	return bootstrap_string

# A function to sort days based on their id (as integer)
def getKey(item):
	return int(item[0])

# Custom template tag to returns days in a structured way
# Used in template to build the table
@register.simple_tag(takes_context=True)
def days_table(context):
	days = context['days']
	result = {}
	week = 1
	for i in range(1,50):
		if not str(week) in result:
			result[str(week)] = {}
		result[str(week)][str(i)] = days.get(str(i))
		if len(result[str(week)]) == 7:
			result[str(week)] = sorted(result[str(week)].items(), key=getKey)
			week = week + 1
	
	return sorted(result.items())
			