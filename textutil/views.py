#this is file created by diksha

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')
   # return HttpResponse("home")

def NavBar(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)



def analyze(request):
    #get the text:
   djtext=request.GET.get('text','default')

   #check chekcboxes values
   removepunc=request.GET.get('removepunc','off')
   fullcapital=request.GET.get('fullcapital','off')
   newlineremove=request.GET.get('newlineremove','off')
   extraspaceremove=request.GET.get('extraspaceremove','off')
   

   
   

   #check which checkbox is on
   if removepunc=="on":
       #analyzed=djtext
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
       analyzed=""
       for char in djtext:
           if char not in punctuations:
               analyzed=analyzed+ char
       params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
       #analyze the text
       return render(request,'analyze.html',params)

   elif (fullcapital=="on"):
       analyzed=""
       for char in djtext:
           analyzed=analyzed+ char.upper()
       params={'purpose':'Capitalize whole sentence','analyzed_text':analyzed}
       #analyze the text
       return render(request,'analyze.html',params)
       
   elif (newlineremove=="on"):
       analyzed= " "
       for char in djtext:
           if char != "\n" and char!="\r":
               analyzed=analyzed + char
       params={'purpose':'removed new lines','analyzed_text':analyzed}
       #analyze the text
       return render(request,'analyze.html',params)

   elif (extraspaceremove=="on"):
       analyzed=""
       for index, char in enumerate(djtext):
           if not(djtext[index] == " "  and djtext[index+1] == " "):
                analyzed = analyzed + char
       params={'purpose':'extra space remover','analyzed_text':analyzed}
       #analyze the text
       return render(request,'analyze.html',params)
    
   else:
       return HttpResponse("error")

'''
def removepunc(request):
    #get the text:
   djtext=request.GET.get('text','default')
   print(djtext)

   #analyze the text
    return HttpResponse("Remove Punctuation")

def firstcap(request):
    return HttpResponse("capitalize the first")

def newlineremove(request):
    return HttpResponse("remove new line")

def spaceremove(request):
    return HttpResponse("remove spaces <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("char count")
'''

#Diksha code for learning how to open links,how to direct to any link:

#def index(request):
#   return HttpResponse('''<h1>hllo diksha</h1> <a href="https://www.sas.com/en_in/insights/analytics/machine-learning.html"> Django With diksha </a>''')

#def about(request):
#    return HttpResponse("about pg is here!!!")

