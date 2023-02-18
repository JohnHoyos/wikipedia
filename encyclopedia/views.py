from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from . import util
from django.core.files.storage import default_storage
import re
from random import choice
markdowner = Markdown()

class NewForm(forms.Form):
    form = forms.CharField(label="search")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def random(request):
    return render(request, "encyclopedia/random.html")

def newpage(request):
    if request.method == "POST" and request.POST['title']!="" and request.POST['content'] != "" : 
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        return render(request, "encyclopedia/entrypage.html",{        
        'entry': markdowner.convert(content),
        "title": title
    })
    else:
        return render(request, "encyclopedia/newpage.html")
   
def entrypage(request, title):
    data = util.get_entry(title)
    if data == None:
        data = "Request page was not found"
    return render(request, "encyclopedia/entrypage.html",{        
        'entry': markdowner.convert(data),
        "title": title
    })

def find(request):   
    value = util.list_entries()
    list_of_similar = []
    final = []
    if request.method == "POST": 
        string = request.POST['search']
        string = str(string)
        data = util.get_entry(string)
    if data == None:        
        for entry in value:
            string = string.upper()        
            entry = entry.upper() 
            if string in entry:
                list_of_similar.append(entry)                
            else:
                data = "Request page was not found"      
    for item in list_of_similar:
        item = item.capitalize()
        final.append(item)
        #import pdb;pdb.set_trace()             
    if not list_of_similar:
        return render(request, "encyclopedia/entrypage.html",{        
                    'entry': markdowner.convert(data),
                    "title": request.POST['search']
                })
    else:
        return render(request, "encyclopedia/index.html", {
                "entries": final
                })
def editpage(request):
    if request.method == "POST":
        title = request.POST['edititem']
        content = util.get_entry(title) 
        #import pdb;pdb.set_trace()    
    return render(request, "encyclopedia/editpage.html",{
        "title" : title,
        "content" : content
    })
def random(request):
    title = choice(util.list_entries())
    data = util.get_entry(title)
    #import pdb;pdb.set_trace()
    return render(request, "encyclopedia/random.html",{        
        'entry': markdowner.convert(data),
        "title": title
        
    })