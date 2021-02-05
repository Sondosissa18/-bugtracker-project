"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.urls import path, include

from django.views.generic.base import TemplateView

from bugtracker_app import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', views.index_view, name='home'),
    path('', views.login_view, name='login'),
    path('admin/', admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("addticket/", views.add_ticket, name="add_ticket"),
    path("editticket/<int:ticket_id>/", views.edit_ticket, name="edit_ticket"),
    path("assignperson/<int:ticket_id>/", views.status_view, name="status_view"),
    # path("actionview/<int:ticket_id>/", views.action_view, name="action_view"),
    path("ticket/<int:ticket_id>/", views.ticket_detail, name="ticketdetail"),
    path("user/<int:user_id>/", views.user_detail, name="user_detail"),
    path("completed/<int:ticket_id>/", views.Complete_ticket, name="assign_ticket_as_completed"),
    path("invalid/<int:ticket_id>/", views.Invalid_ticket, name="assign_ticket_as_invalid"),
    path("assigntickettoyou/<int:ticket_id>/", views.assign_ticket_to_you, name="assign_ticket_to_you"),
]
