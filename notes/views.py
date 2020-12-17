from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import User,Label,Note
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    current_user=User.objects.get(id=request.user.id)
    mynotes=Note.objects.all().filter(users_note=current_user).exclude(archive=True)
    return render(request,'notes/index.html',{
        'mynotes':mynotes
    })

def create_note(request):
    print(User.objects.get(username=request.user.username))
    if request.method=="POST":
        title=request.POST['title']
        note=request.POST['note']
        mylabels=request.POST.getlist('mylabels')
        note_obj=Note(users_note=User.objects.get(username=request.user.username),title=title,note=note)
        note_obj.save()
        if len(mylabels)!=0:
            temp_note=Note.objects.get(id=note_obj.id)
            for i in mylabels:
                temp_note.label.add(Label.objects.get(label=i))
        return HttpResponseRedirect(reverse('index'))
    user_obj=User.objects.get(username=request.user.username)
    labels=Label.objects.all().filter(users_label=user_obj)
    return render(request,'notes/create_note.html',{
        'labels':labels
    })

def labled_notes(request,label=None):
    current_user=User.objects.get(id=request.user.id)
    labled_notes=current_user.user_notes.all().exclude(archive=True)
    if label!='all':
        temp_label_obj=Label.objects.get(label=label)
        labled_notes=temp_label_obj.labled_notes.all().exclude(archive=True)
    return render(request,'notes/labled_notes.html',{
        'labels':current_user.user_labels.all(),
        'labled_notes':labled_notes
    })

def create_label(request):
    l=Label(label=request.POST['labelname'],users_label=User.objects.get(id=request.user.id))
    l.save()
    return HttpResponseRedirect(reverse('labled_notes',args=('all',)))

def delete_label(request):
    label_list_for_deletion=request.POST.getlist('labels_to_delete')
    if label_list_for_deletion!=[]:
        for i in label_list_for_deletion:
            Label.objects.get(label=i).delete()
    return HttpResponseRedirect(reverse('labled_notes',args=('all',)))



def delete_note(request,id):
    Note.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))


def my_archived_notes(request):
    current_user=User.objects.get(id=request.user.id)
    my_archived_notes=Note.objects.all().filter(users_note=current_user).exclude(archive=False)
    return render(request,'notes/archived_notes.html',{
        'my_archived_notes':my_archived_notes
    })

def archive_note(request,id):
    a=Note.objects.get(id=id)
    a.archive=True
    a.save()
    return HttpResponseRedirect(reverse('index'))

def unarchive_note(request,id):
    a=Note.objects.get(id=id)
    a.archive=False
    a.save()
    return HttpResponseRedirect(reverse('index'))


def register(request):
    #if user is logged in 
    if request.user.is_authenticated:
        return render(request,'notes/base.html')

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "notes/register.html", {
                "message": "username already taken !"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request,'notes/register.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "notes/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "notes/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))