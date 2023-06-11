from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.



class NewtaskForm(forms.Form):
    task = forms.CharField(label= "New Form")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "taskapp/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewtaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("taskapp:index"))
        else:
            return render(request, "taskapp/add.html" , {
                'form': form
            })
    return render(request, "taskapp/add.html", {
       "form": NewtaskForm()
    })
