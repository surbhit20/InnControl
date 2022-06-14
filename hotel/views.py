from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from hotel.models import Info
from django.utils import timezone



def index(request):
    return render(request, 'hotel/FrontPage.html')

def rooms(request):
    q=Info(destination=request.GET['hotels'], checkin=request.GET['trip-start'], checkout=request.GET['trip-end'], rooms=request.GET['rooms'], adult=request.GET['adults'], child=request.GET['children'], pan=request.GET['pan'])
    q.save()
    request.session['pan'] = request.GET['pan']
 
    return render(request, 'hotel/RoomPage.html')

def book(request):
    
    # print(q.pan)
    # print(q.checkin)
    # q.pan="qqqqqttttt"
    # q.save()

    return render(request, 'hotel/Booking.html')

def thank(request):
    print(request.session['pan'])
    q = get_object_or_404(Info, pan=request.session['pan'])
    q.first = request.GET['first_name']
    q.last = request.GET['last_name']
    q.email = request.GET['mail']
    q.phone = request.GET['phone']
    q.save()
    return render(request, 'hotel/thanks.html')