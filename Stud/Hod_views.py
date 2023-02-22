
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


#from django.template import engine
#from django.template import Engine, EngineHandler, engines
from app.models import Course, CustomUser,Session, Student,Staff, Subject
from django.contrib import messages

from das.models import DimAgroAssurance




#@login_required(login_url='/')
def Home(request):
    dataObject=DimAgroAssurance.objects.all().count()
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()
    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()
    
    
    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
        'dataObject':dataObject,
    }
    return render(request,'Hod/home.html',context)

