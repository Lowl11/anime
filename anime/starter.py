from django.shortcuts import render, redirect

class Starter:
    @staticmethod
    def start_from():
        return 'watch'
    
    @staticmethod
    def not_found_method():
        return redirect('/not-found/')
