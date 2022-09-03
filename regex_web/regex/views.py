from django.shortcuts import render
import re
# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'regex/home.html')
    
    if request.method == 'POST':
        s = request.POST.get("string")
        r = request.POST.get("regex")
        x = re.search(r,s)
        return render(request,'regex/home.html', {'msg':x})
