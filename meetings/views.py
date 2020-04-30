from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meeting, Room
# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id) #Meeting.objects.get(pk=id)
    return render (request, "meetings/detail.html", {"meeting": meeting})

def drooms(request):
    rooms = Room.objects.all()
    return render(request,"meetings/rooms.html", {"rooms":rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        #form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else: #the request method will be GET
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})