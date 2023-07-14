from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from demoapp.forms import LoginForm, studentloginform, notificationform, StdntComplaintForm
from demoapp.models import studentlogin, notificationadd, StdntComplaint


# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    form = LoginForm()
    form1 = studentloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = studentloginform(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            student = form1.save(commit=False)
            student.user = user
            student.save()
            return redirect(loginview)
    return render(request, 'registration.html', {'form': form, 'form1': form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
             login(request, user)
             return redirect('adminhome')

        if user is not None and user.is_student:
            if user.student.status == True:

                login(request, user)
                return redirect('studenthome')

        else:
            messages.info(request, 'Invalid Credentials')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('loginview')

@login_required(login_url='loginview')
def adminhome(request):
    return render(request, 'admin/dash.html')

@login_required(login_url='loginview')
def studenthome(request):
    return render(request, 'student/dash.html')


def studentview(request):
    data=studentlogin.objects.all()
    print(data)
    return render(request,'admin/viewstudents.html',{'data':data})

def approve_student(request,id):
    student = studentlogin.objects.get(id=id)
    student.status = True
    student.status = 1
    student.save()
    messages.info(request, 'accept teacher login')
    return redirect('studentview')

# Reject student
def reject_student(request, id):
    student = studentlogin.objects.get(id=id)
    if request.method == 'POST':
        student.status = 2
        student.save()
        messages.info(request,'rejected teacher login')
    return redirect('studentview')

def addnotification(request):
    form = notificationform()
    u = request.user
    if request.method=='POST':
        form = notificationform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('viewnotification')
    return render(request,'admin/addnotification.html',{'form':form})

def viewnotification(request):
    u = request.user
    data = notificationadd.objects.filter(user=u)
    return render(request,'admin/viewnotification.html',{'data':data})

def sviewnotification(request):
    u = request.user
    data = notificationadd.objects.all()
    return render(request,'student/sviewnotification.html',{'data':data})

def complaint_add_student(request):
    form = StdntComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = StdntComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('complaint_studentview')
    else:
        form = StdntComplaintForm()
    return render(request, 'student/complaintadd.html', {'form': form})


def complaint_studentview(request):
    n = StdntComplaint.objects.filter(user=request.user)
    return render(request, 'student/viewcomplaint.html', {'complaint': n})


def stdntcomplaint_view(request):

    # n = TchrComplaint.objects.all()
    n = StdntComplaint.objects.all()

    return render(request, 'admin/viewstdntcomplaint.html', {'complaint': n})

# Reply Complaints
def reply_studntcomplaint(request, id):
    complaint = StdntComplaint.objects.get(id=id)
    # complaint2 = StdntComplaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('stdntcomplaint_view')
    return render(request, 'admin/replystdntcomplaint.html', {'complaint': complaint})

