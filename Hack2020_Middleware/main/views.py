from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Vessel
#from .serializers import MapSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.utils.datastructures import MultiValueDictKeyError
# from django.views.generic import FormView
# from main.forms import MapForm
import requests

def index(request):
    return render(request, 'main/index.html')


def register(request):
    return render(request, 'main/register_user.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pwd']

        # if request.POST['remember'] =='on':
        newUser = User.objects.create_user(username, password=password)
        newUser.save()
        return render(request, 'main/index.html')


    else:
        return HttpResponseRedirect(reverse('register'))


def register_vessel(request):
    if request.method == 'POST':
        vName = request.POST['vName']
        vLength = request.POST['vlength']
        vBreadth = request.POST['vbreadth']
        vMaxDraft = request.POST['vMaxDraft']
        vSpeed = request.POST['vSpeed']
        user = request.user
        newVessel = Vessel(
            user=user,
            vesselLength=vLength,
            vesselBreadth=vBreadth,
            vesselMaxDraft=vMaxDraft,
            vesselSpeed=vSpeed,
            vesselName=vName
        )
        newVessel.save()
        return render(request, 'main/home_view.html',
                      {'message': 'Your vessel has been registered.', 'vessel': Vessel.objects.get(vesselName=vName)})
    else:
        return render(request, 'main/register_vessel.html')


def loginHome(request):
    return render(request, 'main/login_user.html')


def login_view(request):
    username = request.POST.get('uname')
    password = request.POST.get('pwd')
    user = User.objects.get(username=username)

    print(user)
    print(username,password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('home_view'))
    else:
        return render(request, "main/login_user.html", {"message": "Invalid credentials."})


def logOut(request):
    logout(request)
    return render(request, 'main/index.html', {'message': 'You have been logged out.'})


def home_view(request, *args):
    if not request.user.is_authenticated:
        return render(request, 'main/login_user.html', {'message': None})
    context = {
        'user': request.user,
    }

    if request.method=='post':
        return render(request, 'main/home_view.html')
    else:
        return render(request, 'main/home_view.html')


def vessels_view(request):
    vessels = Vessel.objects.filter(user=request.user)

    if vessels is not None:
        context = {
            'vessels': vessels}

        return render(request, 'main/vessels_view.html', context)
    else:
        return render(request, 'main/vessels_view.html', {'msg': 'No registered vessels.'})


def vessel_details(request, vessel_id):
    pass

def weatherFinder(request):

    type = 'windSpeed'
    if request.method=="POST":
        lat = (request.POST.get('lat'))
        lng = (request.POST.get('lng'))

        json_data = weatherAPI(lat,lng,type)

        return json_data
    else:
        pass



def weatherAPI(lat,lng, type):

        response = requests.get('https://api.stormglass.io/v2/weather/point',
        params={
            'lat':lat,
            'lng':lng,
            'params':type,
        },
        headers={
            'Authorization': 'd3488c5e-951d-11ea-af71-0242ac130002-d3488d12-951d-11ea-af71-0242ac130002'
        })
        json_data = response.json()
        return json_data




        #return render (request,'main/weatherAPI.html', data=json_data)
#def voyage(request):
#    return render(request, 'main/voyage.html')


#def voyage_view(request, vessel_id):
#    pass
#
# class mapview(FormView):
#     form_class = MapForm
#     template_name = 'main/mapview.html'
