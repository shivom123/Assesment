from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def Register(request):
	if request.method == "POST":
		params = request.POST
		first_name, last_name, = params.get('first_name', ''), params.get('last_name', ''),
		password, email = params.get('password', ''), params.get('email')
		avatar = request.FILES['avatar']
		
		if not User.objects.filter(username=first_name +' '+ last_name).exists():
			if not User.objects.filter(email=email).exists():
				user_obj = User.objects.create(username=first_name +' '+ last_name, first_name=first_name, last_name=last_name, password=password, email=email)
				user_obj.save()
				Profile.objects.create(user_id=user_obj.id, avatar=avatar)
				return render(request, "User/login.html")
			else:
				messages.warning(request, "Already registered with this email.")
				return render(request, "User/register.html")
		else:
			messages.warning(request, "username already taken.")
			return render(request, "User/register.html")
	return render(request, "User/register.html")


def loginView(request):
	if request.method == "POST":
		params = request.POST
		email = params.get('email', None)
		password = params.get('password', None)
		try:
			auth_user = User.objects.get(email=email)
		except Exception as e:
			messages.error(request, "Your are not registered user.")
			return render(request, 'User/login.html')
		
		if password == auth_user.password:
			user = authenticate(username=auth_user.username, password=auth_user.password)
			login(request, user)
			try:
				profile_obj = Profile.objects.get(user_id=auth_user.id)
				context = {
					"username":auth_user.username,
					"email":auth_user.email,
					"first_name":auth_user.first_name,
					"last_name":auth_user.last_name,
					"profile_image": profile_obj.avatar,
				}
				return render(request, 'User/profile.html',{"profile_data":context})
			except Exception as e:
				messages.warning(request, "Your do no have any profile yet.")
				return render(request, 'User/login.html')
		else:
			messages.warning(request, "Please enter correct password.")
			return render(request, 'User/login.html')
	else:
		return render(request, 'User/login.html')
			










		# try:
		# 	auth_user = User.objects.get(email=email)
		# 	has_password = check_password(password, auth_user.password)
		# 	if has_password:
		# 		if auth_user.is_active:
		# 			login(request, auth_user)
		# 			messages.success(request, 'Welcome to Skill-Up Leave Portal.')
		# 			con
		# 			return redirect("/")
		# 		else:
		# 			messages.warning(request, 'Your account has been disable. please contact to admin.')
		# 			return render(request, 'login.html',{"form":form})
		# 	else:
		# 		print("password not correct")
		# 		messages.warning(request, 'Please enter correct password.')
		# 		return render(request, 'login.html')
		# except MyUser.DoesNotExist:
		# 	print("User Not found!")
		# 	messages.warning(request, 'Looks like your are not registered employee. please contact to admin!')
		# 	return render(request, 'login.html',{"form":form})
		


def UserProfile(request):
	return render(request, "User/profile.html")