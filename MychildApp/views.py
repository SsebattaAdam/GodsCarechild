from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Activities, Posts
from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse, JsonResponse

from .forms import ActivitiesForm, PostsForm
# Create your views here.


def index(request):
    posts = Posts.objects.all()
    activities = Activities.objects.all()
    return render(request, 'index.html', {'posts': posts, 'activities': activities})


def about(request):
    # return HttpResponse("Hello, world. You're at the MyChildApp about.")
    return render(request, 'about.html')


def classes(request):
    posts = Posts.objects.all()
    return render(request, 'classes.html', {'posts': posts})


def contact(request):
    return render(request, 'contact.html')


def appointment(request):
    return render(request, 'appointment.html')


def facility(request):
    return render(request, 'facility.html')


def ativities(request):
    activities = Activities.objects.all()
    return render(request, 'ativities.html', {'activities': activities})


def calltoaction(request):
    return render(request, 'call-to-action.html')


def adminLogin(request):
    return render(request, 'admin/login.html')


def homapage(request):
    return render(request, 'admin/sidebar.html')


def submitLoginDetails(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('password')
        # Check if user exists in the database
        if User.objects.filter(email=email, password=password).exists():

            return redirect('homapage')
        else:

            return render(request, 'admin/login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'admin/login.html')


# adminrouts
def addPost(request):
    return render(request, 'admin/add_post.html')


def addActivity(request):
    return render(request, 'admin/activites.html')


def tables(request):
    return render(request, 'admin/tables.html')


def submit_activity(request):
    if request.method == 'POST':
        form = ActivitiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homapage')  # Redirect to a success page
    else:
        form = ActivitiesForm()
    return render(request, 'admin/sidebar.html', {'form': form})


def posts(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to home page after form submission
            return redirect('homapage')
    else:
        form = PostsForm()
    return render(request, 'admin/sidebar.html', {'form': form})


def display_tables(request):
    activities = Activities.objects.all()
    posts = Posts.objects.all()

    return render(request, 'admin/tables.html', {'activities': activities, 'posts': posts})


def edit_post(request, post_id):
    post = Posts.objects.get(pk=post_id)
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('addPost')
    else:
        form = PostsForm(instance=post)
    return render(request, 'add_post.html', {'form': form})


def delete_activity(request, id):
    try:
        activity = Activities.objects.get(id=id)
        activity.delete()
        # Redirect to the homepage
        return redirect('homapage')
    except Activities.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Activity not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


def delete_post(request, id):
    try:
        post = Posts.objects.get(id=id)
        post.delete()
        return redirect('homapage')  # Redirect to the homepage
    except Posts.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Post not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            settings.EMAIL_HOST_USER,  # From email
            ['adamssebatta@gmail.com'],  # To email
            fail_silently=False,
        )
        messages.success(request, 'Email sent successfully')
        return redirect('contact')  # Redirect to contact page

    return HttpResponse('Failed to send email')
