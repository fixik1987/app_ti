from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def user_author_sign_in(request):
    data = {
        'id': '',
        'error': ''
    }
    error = ''
    if request.method == 'POST':
        got_input_data_name = request.POST.get('name_field')
        got_input_data_password = request.POST.get('password_field')
        list_users_found = User.objects.filter(name=got_input_data_name)
        if list_users_found.count() > 0:
            if got_input_data_password == list_users_found[0].password:
                data = {
                    'id': list_users_found[0].id,
                    'error': error
                }
                return redirect('about')
        else:
            error = 'Wrong data in the Form'
            data = {
                'id': '',
                'error': error
            }
    return render(request, 'user/user_author_sign_in.html', data)


def user_author_login(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_author_sign_in')
        else:
            error = 'Wrong data in the Form'

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'user/user_author_login.html', data)
