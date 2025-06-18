from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "website"




# from django.contrib.auth import get_user_model
# User = get_user_model()
# user = User.objects.get(username="tim")

# print("Hashed password:", user.password)  
# print("Check password:", user.check_password("tim"))  
