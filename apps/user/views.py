import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from apps.user.models import User
from apps.user.forms import LoginForm, UserForm
from apps.user.mixins import LoginRequiredUserIstaffOrIsactiveRequiredMixin, UserPermissionRequiredMixin

# Create your views here.

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if (request.user.is_authenticated):
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

class Logout(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class UsersList(LoginRequiredUserIstaffOrIsactiveRequiredMixin, UserPermissionRequiredMixin, TemplateView):
    permission_required = ('user.view_user', 'user.add_user', 'user.change_user', 'user.delete_user')
    template_name = 'user/users_table.html'

class UsersTable(LoginRequiredUserIstaffOrIsactiveRequiredMixin, UserPermissionRequiredMixin, ListView):
    permission_required = ('user.view_user', 'user.add_user', 'user.change_user', 'user.delete_user')
    model = User

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = {}
        context['users'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        if (request.is_ajax()):
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('user:users_list')

class CreateUser(LoginRequiredUserIstaffOrIsactiveRequiredMixin, UserPermissionRequiredMixin, CreateView):
    permission_required = 'user.add_user'
    model = User
    form_class = UserForm
    template_name = 'user/create_user.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, request.FILES)
            if (form.is_valid()):
                new_user = self.model(
                    username = form.cleaned_data['username'],
                    name = form.cleaned_data['name'],
                    lastname = form.cleaned_data['lastname'],
                    email = form.cleaned_data['email'],
                    image = form.cleaned_data['image']
                )
                new_user.set_password(form.cleaned_data['password1'])
                new_user.save()
                message = f'Successfully {self.model.__name__} registered.'
                error = 'There are no errors.'
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 201
                return response
            else:
                message = f'Errorful {self.model.__name__} register.'
                error = form.errors
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('user:users_list')

class UpdateUser(LoginRequiredUserIstaffOrIsactiveRequiredMixin, UserPermissionRequiredMixin, UpdateView):
    permission_required = 'user.change_user'
    model = User
    form_class = UserForm
    template_name = 'user/update_user.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, request.FILES, instance=self.get_object())
            if (form.is_valid()):
                form.save()
                message = f'Successfully {self.model.__name__} updation.'
                error = 'There are no errors.'
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 201
                return response
            else:
                message = f'Errorful {self.model.__name__} updation.'
                error = form.errors
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('user:users_list')

class DeleteUser(LoginRequiredUserIstaffOrIsactiveRequiredMixin, UserPermissionRequiredMixin, DeleteView):
    permission_required = 'user.delete_user'
    model = User
    template_name = 'user/delete_user.html'

    def delete(self, request, *args, **kwargs):
        if (request.is_ajax()):
            user = self.get_object()
            user.delete()
            message = f'Successfully {self.model.__name__} elimination.'
            error = 'There are no errors.'
            response = JsonResponse({'message':message, 'error':error})
            response.status_code = 201
            return response
        else:
            return redirect('user:users_list')