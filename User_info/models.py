# from django.db import models
# from django.contrib.auth.models import User

# GENDER_CHOICE = (
#     ('male','male'),
#     ('female','female'),
#     ('other','other')
# )

# class UserType(models.Model):
#     user = models.ForeignKey(to=User, verbose_name=_("user type"), on_delete=models.CASCADE)
#     is_patient = models.BooleanField(default=False, null=True)
#     is_doctor = models.BooleanField(default=False, null=True)
#     is_staff = models.BooleanField(default=False, null=True)
#     is_medicos = models.BooleanField(default=False, null=True)


# class UserProfileCommonField(models.Model):
#     firstName = models.CharField(_(""), max_length=50, null=True)
#     lastName = models.CharField(_(""), max_length=50, null=True)
#     phoneNo = models.CharField(_(""), max_length=50, null=False, unique=True)
#     gender = models.CharField(choices=GENDER_CHOICE, max_length=50)
#     DOB = models.DateField(auto_now_add=True, null=True)
#     aboutMe = models.TextField(null=True, blank=True)
#     photo = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
#     # address