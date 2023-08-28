from typing import Any, Dict
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.base import TemplateView,RedirectView,View
from django.db.models import Q
from django.core.paginator import Paginator


from .models import Employee


class DisplayClassView(View):
    def get(self,Request):
        data = Employee.objects.all().order_by("-id")
        paginator = Paginator(data,2)
        page_number = Request.GET.get("page")
        data_obj = paginator.get_page(page_number)
        return render(Request,"index.html",{'data':data_obj})
    



class EmployeePostClassView(TemplateView):
    template_name = 'add.html'

    def post(self,Request):
        if Request.method=="POST":
            name = Request.POST.get("name")
            email = Request.POST.get("email")
            phone = Request.POST.get("phone")
            dsg = Request.POST.get("dsg")
            salary = Request.POST.get("salary")
            city = Request.POST.get("city")
            state = Request.POST.get("state")

            try:
                emp = Employee()
                emp.name = name
                emp.email = email
                emp.phone = phone
                emp.dsg = dsg
                emp.salary = salary
                emp.city = city
                emp.state = state
                emp.save()
                return HttpResponseRedirect("/")
            except:
                pass
        else:
            return render(Request,"add.html")
        

class EmployeeDeleteView(RedirectView):
    url = "/"
    def get_redirect_url(self,*args,**kwargs):
        id = kwargs['id']
        try:
            Employee.objects.get(id=id).delete()
        except:
            pass
        return super().get_redirect_url(*args,**kwargs)
    

class EmployeeUpdateView(View):
    template_name = "update.html"
    def get(self,Request,id):
        data = Employee.objects.get(id=id)
        return render(Request,"update.html",{"data":data})

    def post(self,Request,id):
        if Request.method=="POST":
            name = Request.POST.get("name")
            email = Request.POST.get("email")
            phone = Request.POST.get("phone")
            dsg = Request.POST.get("dsg")
            salary = Request.POST.get("salary")
            city = Request.POST.get("city")
            state = Request.POST.get("state")

            try:
                emp = Employee.objects.get(id=id)
                emp.name = name
                emp.email = email
                emp.phone = phone
                emp.dsg = dsg
                emp.salary = salary
                emp.city = city
                emp.state = state
                emp.save()
                return HttpResponseRedirect("/")
            except:
                pass
        else:
            return render(Request,"add.html")
        


class EmployeeSearchView(View):
    def post(self,Request):
        if Request.method=="POST":
            search = Request.POST.get('search')
            data = Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(phone__icontains=search)|Q(dsg__icontains=search)|Q(city__icontains=search)|Q(state__icontains=search))
            paginator = Paginator(data,2)
            page_number = Request.GET.get("page")
            data_obj = paginator.get_page(page_number)
            return render(Request,'index.html',{'data':data_obj})
        else:
            return HttpResponseRedirect("/")