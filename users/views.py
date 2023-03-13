from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mbasubmission.utils import get_totals
from mbasubmission.models import Application, Document

def LoginUser(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'this email does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'dashboard')

        else:
            messages.error(request,'your email or password is invalid')
    
    return render(request, 'users/login.html')


def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'you signed out!')
    return redirect('login')




@login_required(login_url="login")
def Dashboard(request):
    page = 'dashboard'
    context = {
        'page': page,
        'totals': get_totals(),
    }
    return render(request, 'users/dashboard.html',context)


@login_required(login_url="login")
def Applications(request):
    page = 'applications'
    context = {
        'page': page,
        'pending_applications': Application.objects.filter(application_state=Application.ApplicationState.PENDING),
        'totals': get_totals(),
    }
    return render(request, 'users/applications.html', context)


@login_required(login_url="login")
def AcceptedApplications(request):
    context = {
        'accepted_applications': Application.objects.filter(application_state=Application.ApplicationState.OFFER_LETTER_ISSUED),
        'totals': get_totals(),
    }
    return render(request, 'users/accepted_applications.html', context)


@login_required(login_url="login")
def RejectedApplications(request):
    context = {
        'rejected_applications': Application.objects.filter(application_state=Application.ApplicationState.ENROLLMENT_COMPLETE),
        'totals': get_totals(),
    }
    return render(request, 'users/rejected_applications.html', context)


@login_required(login_url="login")
def ApplicationDetail(request, pk):
    page = 'application-detail'
    application = Application.objects.get(id=pk)
    documents = Document.objects.filter(application=application)
    context = {
        'page': page,
        'application': application,
        'documents': documents,
        'totals': get_totals(),
    }
    return render(request, 'users/application_detail.html', context)