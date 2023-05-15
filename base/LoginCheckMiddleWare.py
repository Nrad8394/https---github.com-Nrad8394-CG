from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user
        #Check whether the user is logged in or not
        if user.is_authenticated:
                if modulename == "base.views":
                    pass
                else:
                    return redirect("tracker")
        else:
            if request.path == reverse("login") or request.path == reverse("doLogin") or request.path == reverse("login"):
                pass
            else:
                return redirect("login")

