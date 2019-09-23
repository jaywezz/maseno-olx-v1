from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, LoginForm


class SignUp(FormView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('item_view:profile')
	template_name = 'authentication/index.html'

	def form_valid(self, form):
		form.save()

		username = self.request.POST['username']
		password2 = self.request.POST['password2']

		user = authenticate(username=username, password=password2)
		login(self.request, user)

		return redirect('item_view:profile')


"""class UserFormView(View):

	template_name = 'authentication/index.html'

	#Display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	#Process form Data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit= False)

			username = form.cleaned_data['username']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct


			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('item_view:profile')

		return render(request, self.template_name, {'form': form})


"""


class LoginView(View):
	form_class = LoginForm
	template_name = 'login/index.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid:

			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:

				login(request, user)
				return redirect('item_view:welcome_page')
			elif user is None:
				print("no user found")
		return render(request, self.template_name, {'form': form})


def logout_view(request):
	logout(request)

	return render(request, 'logged_out.html')
