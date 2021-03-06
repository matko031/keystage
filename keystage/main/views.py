from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q
from .forms import register_user_form, register_student_form, register_company_form, account_form, CustomUserChangeForm, add_internship_form
from .models import *


lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce pulvinar non nunc eget blandit. Vestibulum semper nisi in vehicula porta. Suspendisse potenti. Maecenas consequat urna at dolor vehicula, id sodales metus dapibus. Maecenas id felis eu ante pellentesque efficitur. Nunc pulvinar condimentum rhoncus. Vivamus tincidunt vitae ex nec vestibulum. Quisque ullamcorper faucibus placerat. Nam tempor velit lacus, non feugiat mi tempor id. Ut interdum vehicula purus, ut dapibus odio. Nullam sit amet felis nec nunc ullamcorper finibus finibus non libero. Morbi non eleifend dolor. Nam tincidunt egestas ipsum vel pulvinar. Sed justo orci, aliquam ut bibendum ut, laoreet vitae ex."

def find_internship(request):

    if request.user.type != 's':
        return redirect('main:homepage')

    student = request.user
    stud_profile = student_profile.objects.get(student=student)
    internships = company_internships.objects.filter(target_study_year = stud_profile.study_year).values()[0]

    return render(request, "main/find_internship.html", {"internships":internships})


def delete_internship(request, internship_id):
    internship = company_internships.objects.get(id=internship_id)
    internship.delete()
    return redirect('main:homepage')

def internships(request):
   current_company = request.user
   internships = company_internships.objects.filter(company=current_company).values('name', 'target_faculty', 'id')

   return render(request, "main/company_internships.html", {"internships":internships})

def add_internship(request):

    form = add_internship_form(request.POST)

    if request.method == 'POST':
        if form.is_valid():

            internship = form.save(commit=False)
            internship.company = request.user
            internship.save()

        return redirect("main:homepage")

    return render(request, "main/add_internship.html", {"form": form})


def account(request):
    user_type = request.user.type
    user = request.user

    if user.type == 'c':
        name = company_profile.objects.get(company = user).name
        info = company_profile.objects.all().filter(company= user).values()[0]
        labels = account_labels.objects.filter(Q(model='company_profile') | Q(model='CustomUser')).values()[0]

        entries_to_remove = ('id', 'company_id')

        for entry in entries_to_remove:
            info.pop(entry, None)

        return render(request, "main/account_company.html", {"name":name, "info": info, 'labels':labels} )

    elif user.type == 's':
        first_name = student_profile.objects.all().get(student = user).first_name
        last_name = student_profile.objects.get(student = user).last_name
        name = first_name + " " + last_name
        info = student_profile.objects.all().filter(student = user).values()[0]
        labels = account_labels.objects.all().filter(Q(model='student_profile') | Q(model='CustomUser')).values()
        print(labels)
        entries_to_remove = ('id', 'student_id')

        for entry in entries_to_remove:
            info.pop(entry, None)

        return render(request, "main/account_student.html", {"name":name, "info": info, 'labels':labels} )




def account_edit(request):

    user = request.user

    form = register_user_form( instance = request.user)

    if request.method == "POST":
        if form.is_valid():
            form.save()

        return redirect("main:homepage")

    return render(request, 'main/account_edit.html', {'form':form})


def homepage(request):

    return render(
        request=request,
        template_name='main/home.html',
        context={"lorem_ipsum":lorem_ipsum }
    )

def register_student(request):

    form1 = register_user_form(request.POST, prefix='register_user')
    form2 = register_student_form(request.POST, prefix='register_student')

    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():

            user = form1.save(commit=False)
            user.type='s'
            user.set_password( form1.cleaned_data.get('password') )
            user.save()

            profile = form2.save(commit=False)
            profile.student = user
            profile.save()

            username = form1.cleaned_data.get('username')
            messages.success(request, f"New Account Created:{username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('main:homepage')

        elif not form1.is_valid():
            messages.error(request, "register_user not_valid")
        else:
            messages.error(request,"register_student not valid")

    return render(
        request,
        "main/register_user.html",
        context={"forms":[form1 ]}
       )



def register_company(request):

    form1 = register_company_form(request.POST, prefix='register_company')
    form2 = register_user_form(request.POST, prefix='register_user')

    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():

            user = form2.save(commit=False)
            user.type='c'
            user.set_password( form2.cleaned_data.get('password') )
            user.save()

            profile = form1.save(commit=False)
            profile.company = user
            profile.save()

            username = form1.cleaned_data.get('username')
            messages.success(request, f"New Account Created:{username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('main:homepage')

        elif not form1.is_valid():
            messages.error(request, "register_user not_valid")
        else:
            messages.error(request,"register_student not valid")

    return render(
        request,
        "main/register_user.html",
        context={"forms":[form1, form2]}
       )



def register(request):
    return render(request, 'main/register.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid() or True:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")


    form = AuthenticationForm()
    return render(
        request,
        'main/login.html',
        {'form':form}
    )


