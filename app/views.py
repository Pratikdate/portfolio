from django.shortcuts import redirect, render
from .models import Personal_About_Me,Professional_About_Me,Testimonials,My_Service,My_Works,Messages,Skill,Messages
from .form import MessageForm,TestimonialForm


def home(request):
    personalInfo = Personal_About_Me.objects.all()
    Professional_About_Me_ = Professional_About_Me.objects.all()
    Testimonial = Testimonials.objects.all()
    skill = Skill.objects.all()
    half = (len(skill) + 1) // 2  # Calculate the split point
    skills_col1 = skill[:half]
    skills_col2 = skill[half:]

    My_Service_ = My_Service.objects.all()
    My_Works_ = My_Works.objects.all()


    context = { "personalInfo":personalInfo.get(Name="Pratik Date"),'Professional_About_Me':Professional_About_Me_[0],"Testimonials":Testimonial,'skills_col1': skills_col1,
        'skills_col2': skills_col2,'My_Service':My_Service_,'My_Works':My_Works_}
   
    return render(request, 'index.html',context=context)


def MessageView(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
           
            form.save()
            return redirect('/')

        else:
            print('Error')

        
    

def TestimonialView(request):
    if request.method == 'POST':
        testimonial= TestimonialForm(request.POST,request.FILES)
        print(request.FILES)
        if testimonial.is_valid():
           
            testimonial.save()
            return redirect('/')

        
        
    
