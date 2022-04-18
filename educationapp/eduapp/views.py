from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from.models import place

#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
   # res=x+y
  #  return render(request,"result.html",{'result':res})

def demo(request):
    obj=place.objects.all()

    return render(request,'index.html',{'result':obj})


#def demo(request):
  #  name="india"
   # return render(request,'home.html',{'obj':name})

#def about(request):
   # return render(request,'about.html')

#def contact(request):
 #   return HttpResponse(request,'this is my contact')