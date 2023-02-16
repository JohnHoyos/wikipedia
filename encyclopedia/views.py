from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from . import util
from django.core.files.storage import default_storage
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
    return render(request, "encyclopedia/newpage.html")

def entrypage(request, title):
    data = util.get_entry(title)
    return render(request, "encyclopedia/entrypage.html",{        
        'entry': markdowner.convert(data),
        "title": title
    })

def find(request):   
    if request.method == "POST":        
        data = util.get_entry(request.POST['search'])        
    return render(request, "encyclopedia/entrypage.html",{        
        'entry': markdowner.convert(data),
        "title": request.POST['search']
    })
   
