from django.shortcuts import render



def home(request):
    print('home do app')
    context = {
            'text': 'Olá home'
        }

    return render(
        request,
        'home/index.html',
        context
    )
