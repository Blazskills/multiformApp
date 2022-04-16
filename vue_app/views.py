from django.shortcuts import render

# Create your views here.

def vue_test(request):
    return render(request, 'vue_app/test.html')

