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
            if user.user_type == "0":
                if modulename == "dashboard.ClientView":
                    pass
                elif modulename == "dashboard.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("client_home")

            elif user.user_type == "1":
                if modulename == "dashboard.HodViews":
                    pass
                elif modulename == "dashboard.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_home")
            
            elif user.user_type == "2":
                if modulename == "dashboard.Manager":
                    pass
                elif modulename == "dashboard.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("manager_home")
            
            elif user.user_type == "3":
                if modulename == "dashboard.Operations":
                    pass
                elif modulename == "dashboard.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("operation_home")
            elif user.user_type == "4":
                if modulename == "dashboard.finance":
                    pass
                elif modulename == "dashboard.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("finance_home")
            else:
                return redirect("login")

        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            else:
                return redirect("login")
