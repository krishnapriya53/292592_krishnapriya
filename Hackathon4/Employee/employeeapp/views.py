from django.shortcuts import render
from django.http import HttpResponse
import random
 
# Create your views here.
def accept_data(request):
    return render(request,"input.html")
 
def result(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name', 'Unknown')
        age = request.POST.get('age', 'Unkown')
        company = request.POST.get('company', 'Unkown')
        gross_salary = float(request.POST.get('gross_salary', 'Unkown'))
        tax = float(request.POST.get('tax', 'Unkown'))
        bonus = float(request.POST.get('bonus', 'Unkown'))
       
        net_salary = gross_salary - tax + bonus
       
        context = {
            'name': name,
            'age' : age,
            'company':company,
            'gross_salary':gross_salary,
            'tax':tax,
            'bonus':bonus,
            'gross_salary':gross_salary,
            'net_salary':net_salary
           
        }
        return render(request, 'output.html', context)
    else:
        return render(request, 'input.html')
def jumble_words(request):
    context = {}
    if request.method == 'POST':
        word = request.POST.get('word', 'unknown')
        temp = list(word)
        random.shuffle(temp)
        word = ''.join(temp)
        context = {
            'word': word
        }
    return render(request, 'jumble.html', context)