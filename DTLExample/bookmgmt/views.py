from django.shortcuts import render

# Create your views here.
def book_list(request):
    books = [
        {"title":"C programming", "author":"ABC","available":False},
        {"title": "C++ programming", "author": "QWE", "available": True},
        {"title":"python programming", "author":"XYZ","available":True},
        {"title":"java programming", "author":"MNO","available":False}
    ]
    return render(request, 'bookmgmt/base.html',{'books':books})
