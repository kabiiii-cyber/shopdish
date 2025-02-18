from django.shortcuts import render

# Create your views here.
#create a function to view webpage

def home(request):
  return render(request,'index.html')


def images(request):
  return render(request,'gallary.html')
