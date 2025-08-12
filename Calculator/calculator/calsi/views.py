from django.shortcuts import render

# Create your views here.
def calculator(request):
    output=""
    if request.method =='POST':
        num1=eval(request.POST.get('fn'))
        num2=eval(request.POST.get('ln'))
        operator=request.POST.get('op')
       
        if operator=="+":
            output=num1+num2
        elif operator =="-":
            output=num1-num2
        elif operator == "*":
            output=num1*num2
        elif operator =="/":
            output=num1/num2
    return render(request,'calsi.html',{'op': output})