from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245056',
        'name': 'Daffa Aqil Mahmud',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
