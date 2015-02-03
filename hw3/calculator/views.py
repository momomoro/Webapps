from django.shortcuts import render

context = {'lastDigit':'0','operator':'+','currDigit':''}


def home_page(request):
	return render(request,'calculator/calculator.html',{'lastDigit':'0','operator':'+','currDigit':''})
	
def calculate(request):
	if context['operator'] == '=' :
		context['currDigit'] = ''
		context['operator'] = '+'
	if context['currDigit'] == 'error':
		context['currDigit'] = ''
		context['lastDigit'] = '0'
		context['operator'] = '+'
	print request.POST
	if 'digit' in request.POST:
		context['currDigit'] = str(context['currDigit']) + str(request.POST['digit'])
		print context
		return render(request,'calculator/calculator.html',context)
	elif 'operator' in request.POST:
		try:
			if context['operator'] == '+':
				context['currDigit'] = int(context['lastDigit']) + int(context['currDigit'])
				context['lastDigit'] = context['currDigit']
				context['operator'] = request.POST['operator']
			elif context['operator'] == '-':
				context['currDigit'] = int(context['lastDigit']) - int(context['currDigit'])
				context['lastDigit'] = context['currDigit']
				context['operator'] = request.POST['operator']
			elif context['operator'] == '*':
				context['currDigit'] = int(context['lastDigit']) * int(context['currDigit'])
				context['lastDigit'] = context['currDigit']
				context['operator'] = request.POST['operator']
			elif context['operator'] == "/":
				context['currDigit'] = int(context['lastDigit']) / int(context['currDigit'])
				context['lastDigit'] = context['currDigit']
				context['operator'] = request.POST['operator']
			if request.POST['operator'] == '=':
				context['lastDigit'] = '0'
				context['operator']= '='
				context['currDigit'] = int(context['currDigit'])
				return render(request,'calculator/calculator.html',context)
			print context
			context['currDigit'] = ''
			return render(request,'calculator/calculator.html',context)
		except ValueError:
			return render(request,'calculator/calculator.html',context)
		except ZeroDivisionError:
			context['currDigit'] = 'error'
			return render(request,'calculator/calculator.html',context)
			

	

