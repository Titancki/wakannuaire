from django.shortcuts import render

# Create your views here.
def exemple(request):
    context = {

    }
    return render(request, "test.html", context)