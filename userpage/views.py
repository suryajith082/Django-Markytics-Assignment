from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . import models


# Create your views here.
def index(request):
    message={"state":"Login"}
    return render(request,"docs.html",message)
def login(request):
    return render(request,"login.html")
def check(request):
    if request.method=="POST":
        username = request.POST["username"]
        password=request.POST["password"]
        useragent = models.MarkyticsUser.objects.filter(name=username, password=password).exists()
        request.session["username"]=username

        if useragent is True:
            #auth.login(request,user)
            message = {"username": username, "useragent": useragent, "state": "Logout", "log":True}
            return render(request,"docs.html",message)
        else:
            messages.info(request,"User does not exist!!")
            return redirect("login")
    else:
        return render(request,"login.html")

def register(request):
    pass

def logout(request):
    return redirect(index)

def reportincident(request):
    username=request.session["username"]
    message={"username":username,"useragent":True,"state":"Logout"}
    return render(request,"reportincident.html",message)
def loggedpage(request):

    username=request.session["username"]
    location = request.POST["location"]
    incidentDepartment = request.POST["incidentDepartment"]
    dateofInc = request.POST["dateofInc"]
    timeofInc = request.POST["timeofInc"]
    incidentLocation = request.POST["incidentLocation"]
    suspectedCause = request.POST["suspectedCause"]
    ImmediateAction = request.POST["ImmediateAction"]
    EnvironmentalIncident = request.POST.get("EnvironmentalIncident")
    InjuryIllness = request.POST.get("InjuryIllness")
    PropertyDamage = request.POST.get("PropertyDamage")
    Vehicle = request.POST.get("Vehicle")
    if Vehicle==None:
        Vehicle="False"
    if PropertyDamage==None:
        PropertyDamage="False"
    if InjuryIllness== None:
        InjuryIllness="False"
    if EnvironmentalIncident == None:
        EnvironmentalIncident="False"
    data = models.IncidentReport(Location=location, Incident_Department=incidentDepartment,
                                 Date_Of_Incident=dateofInc, Time_Of_Incident=timeofInc,
                                 Incident_Location=incidentLocation, Suspected_Cause=suspectedCause,
                                 Immediate_Action=ImmediateAction, Environmental_Incident=EnvironmentalIncident,
                                 Injury_Illness=InjuryIllness, Property_Damage=PropertyDamage,
                                 Vehicle=Vehicle, Reported_By=username)
    data.save()
    message={"username":username,"useragent":True,"state":"Logout"}
    return render(request,"docs.html",message)

