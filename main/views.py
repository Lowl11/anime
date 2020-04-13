from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Аниме онлайн'
    }
    return render(request, 'watch/page.html', context)
