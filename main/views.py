from django.shortcuts import render

def home_view(request):
    pages = [
        {'url': 'page1', 'title': 'Сторінка 1'},
        {'url': 'page2', 'title': 'Сторінка 2'},
        {'url': 'page3', 'title': 'Сторінка 3'},
        {'url': 'page4', 'title': 'Сторінка 4'},
    ]
    return render(request, 'main/home.html', {'title': 'Головна', 'pages': pages})

def page1_view(request):
    return render(request, 'main/page.html', {'title': 'Сторінка 1'})

def page2_view(request):
    return render(request, 'main/page.html', {'title': 'Сторінка 2'})

def page3_view(request):
    return render(request, 'main/page.html', {'title': 'Сторінка 3'})

def page4_view(request):
    return render(request, 'main/page.html', {'title': 'Сторінка 4'})
