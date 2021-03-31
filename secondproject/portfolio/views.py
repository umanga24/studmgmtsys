from django.shortcuts import render

def home_page(request):
    return render(request,'index.html')

def gallery_page(request):
    return render(request,'gallery.html')

def cv_page(request):
    return render(request, 'cv.html')

def contact_page(request):
    return render(request, 'contact.html')

