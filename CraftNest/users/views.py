from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.models import Product
from users.forms import RegisterForm

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_artisan = form.cleaned_data.get('is_artisan')
            user.save()
            return redirect('artisan_dashboard' if user.is_artisan else 'home')


    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def artisan_dashboard(request):
    if not request.user.is_artisan:
        return redirect('home')  # or show access denied message

    products = Product.objects.filter(artisan=request.user.artisanprofile)

    return render(request, 'users/dashboard.html',
    {
        'user': request.user,
        'products': products
    })