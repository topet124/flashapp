from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def divide(request):
    from random import randint
    num1= randint(1,9)
    num2= randint(1,10)
    if request.method== "POST":
        answer= request.POST['answer']
        oldnum1='oldnum1' in request.POST and request.POST['oldnum1']
        oldnum2='oldnum2' in request.POST and request.POST['oldnum2']
        correctanswer=int('0'+oldnum1)/int('0'+oldnum2)
        if not answer:
            myanswer="enter the the answer"
            color="danger"
            return render(request, 'divide.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })

        if float('0'+answer)==correctanswer:
            myanswer='it is corect because '+  oldnum1 + " / " +  oldnum2  + ' = ' +  str(correctanswer)
            color="success"
        else:
            myanswer='incorrect '+  oldnum1 + " / " +  oldnum2  + ' != ' +  str(correctanswer)
            color='danger'
        return render(request, 'divide.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })
    return render(request, 'divide.html',{'num1':num1, 
                                         'num2':num2,})

def subtract(request):
    from random import randint
    num1= randint(0,9)
    num2= randint(1,10)
    if request.method== "POST":
        answer= request.POST['answer']
        oldnum1='oldnum1' in request.POST and request.POST['oldnum1']
        oldnum2='oldnum2' in request.POST and request.POST['oldnum2']
        correctanswer=int('0'+ oldnum1)-int('0'+ oldnum2)
        if not answer:
            myanswer="enter the the answer"
            color="danger"
            return render(request, 'subtract.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })
        if correctanswer==int(answer):
            myanswer='it is corect because '+  oldnum1 + " - " +  oldnum2  + ' = ' +  str(correctanswer)
            color="success"
        else:
            myanswer='incorrect '+  oldnum1 + " - " +  oldnum2  + ' != ' +  str(correctanswer)
            color='danger'
        return render(request, 'subtract.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })
    else:
    
     return render(request, 'subtract.html',{'num1':num1, 
                                         'num2':num2,})

def multiply(request):
    from random import randint
    num1= randint(0,9)
    num2= randint(1,10)
    if request.method== "POST":
        answer= request.POST['answer']
        oldnum1='oldnum1' in request.POST and request.POST['oldnum1']
        oldnum2='oldnum2' in request.POST and request.POST['oldnum2']
        correctanswer=int('0'+ oldnum1)*int('0'+ oldnum2)
        if correctanswer==int(answer):
            myanswer='it is corect because '+  oldnum1 + "*" +  oldnum2  + ' = ' +  str(correctanswer)
            color="success"
        else:
            myanswer='incorrect '+  oldnum1 + " - " +  oldnum2  + ' != ' +  str(correctanswer)
            color='danger'
        return render(request, 'multiply.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })
    return render(request, 'multiply.html',{'num1':num1, 
                                         'num2':num2,})

def add(request):
    from random import randint
    num1= randint(0,9)
    num2= randint(1,10)
    if request.method== "POST":
        answer= request.POST['answer']
        oldnum1='oldnum1' in request.POST and request.POST['oldnum1']
        oldnum2='oldnum2' in request.POST and request.POST['oldnum2']
        correctanswer=int('0'+ oldnum1)+int('0'+ oldnum2)
        if not answer:
            myanswer="enter the the answer"
            color="danger"
            return render(request, 'add.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })
        if correctanswer== int('0'+ answer):
            myanswer='it is corect because '+  oldnum1 + " + " +  oldnum2  + ' = ' +  str(correctanswer)
            color="success"
        else:
            myanswer='incorrect '+  oldnum1 + " + " +  oldnum2  + ' != ' +  str(answer)
            color='danger'
        return render(request, 'add.html',{'answer':answer,
                                         'num1':num1, 
                                         'num2':num2,
                                         'myanswer':myanswer,
                                         'color':color
                                         })
 

    return render(request, 'add.html',{'num1':num1, 
                                         'num2':num2,})
