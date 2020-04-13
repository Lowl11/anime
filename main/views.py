from django.shortcuts import render, redirect
from django.conf import settings

from help.viewmodel import ViewModel

SETTINGS = settings.A_SETTINGS
CONSTANTS = settings.A_CONSTANTS

def home_view(request):
    start_from = SETTINGS['start_from']
    if start_from == 'watch':
        return redirect('/watch/')
    return not_found()

def not_found_view(request):
    vm = ViewModel()
    vm.add_path('main/notfound.html')
    vm.add_object('title', CONSTANTS['not_found_title'])
    return vm.render(request)

def not_found():
    return SETTINGS['not_found_method']()
