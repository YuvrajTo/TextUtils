# Code by Yuvraj Todankar
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# Text Analization


def analyze(request):
    # Get Text
    djtext = request.POST.get('text', 'default')

    # Functions
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    # Logic
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Full Capitalization', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Newline Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on":
        return render(request, "error.html")

    # Output
    return render(request, 'analyze.html', params)
