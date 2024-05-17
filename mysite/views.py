from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext= request.POST.get('text', 'default')

    #Check checkbox values
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')

    #check which checkbox is on
    if removepunc == "on":
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_`~'''
        analyzed = ""
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Puntuations', 'analyzed_text':analyzed}
        #analyze the text
        djtext = analyzed
        
    
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
        #analyze the text
        djtext = analyzed
        
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
                
        params = {'purpose':'New line remover', 'analyzed_text':analyzed}
        #analyze the text
        djtext = analyzed
        
    
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        
        params = {'purpose':'Extra line remover', 'analyzed_text':analyzed}
        #analyze the text
        djtext = analyzed
    
    
    if(removepunc != "on" and newlineremover !="on" and extraspaceremover !="on" and fullcaps !="on"):
        return HttpResponse("No Analyzing Option choosen")



    return render(request, 'analyze.html', params)