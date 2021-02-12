from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.

def home(request):
    form = StudentForm()
    stu = Student.objects.all()
    
    return render(request, 'app1/home.html',{'form': form,'stu':stu})

def stu_data(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST['stuid']
            print("================================",sid)
            name = request.POST['name']
            email = request.POST['email']
            enroll = request.POST['enroll']
            if sid == "":
                student = Student(name=name,email=email,enroll=enroll)
            else:
                student = Student(id=sid,name=name,email=email,enroll=enroll)

            student.save()
            stu = Student.objects.values() 
            student_data = list(stu)
            # print(student_data)
            # print(stu)
            return JsonResponse({'status':'Save','student_data': student_data})
        else:
            return JsonResponse({'status':0})

def stu_del(request):
    if request.method == "POST":
        pk = request.POST['sid']
        print(pk)
        pi = Student.objects.get(pk=pk)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})

def stu_up(request):
    if request.method == "POST":
        id = request.POST['stuid']
        print(id)
        pi = Student.objects.get(pk=id)
        student_data ={"id":pi.id,"name":pi.name,"email":pi.email,"enroll":pi.enroll}       
        return JsonResponse(student_data)
    else:
        return JsonResponse({'status': 0})