from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'CMS'
    }
    return render(request, 'cms/anime.html', context)
