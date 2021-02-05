from bugtracker_app.models import MyUser
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from .forms import  LoginForm, AddTicketForm, EditForm
from django.contrib.admin.views.decorators import staff_member_required
from bugtracker_app.models import MyUser, Ticket
from django.contrib.auth.decorators import login_required
from bugtracker_app.forms import LoginForm , ActionsForm, ActionsdropdownForm
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect



@login_required()
def index_view(request):
    tickets = Ticket.objects.all().order_by('-status')
    # tickets = Ticket.objects.filter(id=ticket_id).first()
    context_dict = {"MyUser": settings.AUTH_USER_MODEL, "tickets": tickets}
    return render(request, 'home.html', context_dict)




@login_required()
def ticket_detail(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    change_person = ActionsForm()
    change_status = ActionsdropdownForm()
    return render(request, "ticket_detail.html", {"ticket": my_ticket, "change_person": change_person, "change_status": change_status})


@login_required()
def user_detail(request, user_id):
    user = MyUser.objects.get(id=user_id)
    curent_user_ticket = Ticket.objects.filter(assigned_to=user_id)
    filed_user_ticket = Ticket.objects.filter(author=user_id)
    completed_user_ticket = Ticket.objects.filter(user_completed_by=user_id)
    return render(request, "user_detail.html", {"author": user, "curent_user_ticket" : curent_user_ticket, "filed_user_ticket": filed_user_ticket, "completed_user_ticket":completed_user_ticket})


'''  *   the current tickets assigned to a user
    *   which tickets that user has filed
    *   which tickets that user completed'''


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("home"))
                )
    form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required()
def edit_ticket(request, ticket_id):
    html = "generic_form.html"
    my_ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_ticket.title = data["title"],
            my_ticket.description = data["description"]
            my_ticket.save()
        return HttpResponseRedirect(reverse("home"))
    form = AddTicketForm()
    return render(request, html, {"form": form})


@login_required()
def add_ticket(request):
    html = "generic_form.html"
    if request.method == "POST":
            form = AddTicketForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                ticket = Ticket.objects.create(
                    title=data["title"],
                    author=request.user,
                    description=data["description"],
                )
                return HttpResponseRedirect(reverse("home"))
    form = AddTicketForm()
    return render(request, html, {"form": form})
 

@login_required()
def status_view(request,ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = ActionsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_ticket.assigned_to = data["chooseperson"]
            my_ticket.status = "in progress"
            my_ticket.save()
        return HttpResponseRedirect(reverse("home"))
            

@login_required()
def assign_ticket_to_you(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    my_ticket.status = "In progress"
    my_ticket.assigned_to = request.user
    my_ticket.user_completed_by = None
    my_ticket.save()
    return HttpResponseRedirect(reverse("home"))


    
@login_required()
def Complete_ticket(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    my_ticket.status = "Done"
    my_ticket.assigned_to = None
    my_ticket.user_completed_by = my_ticket.assigned_to
    my_ticket.save()
    return HttpResponseRedirect(reverse("home"))
  

@login_required()
def Invalid_ticket(request, ticket_id):
    my_ticket = Ticket.objects.get(id=ticket_id)
    my_ticket.status = "Invalid"
    my_ticket.assigned_to = None
    my_ticket.user_completed_by = None
    my_ticket.save()
    return HttpResponseRedirect(reverse("home"))
  