from django.shortcuts import render

def index(reqests):
    return render(reqests, 'index.html')