from django.contrib import admin
from django.urls import path

import bible.core.views

urlpatterns = [
    path('', bible.core.views.index, name='index'),
    path('versicles', bible.core.views.versicles, name='versicles'),
    path('sign-in', bible.core.views.signin, name='signin'),
    path('sign-up', bible.core.views.signup, name='signup'),
    path('reset-password', bible.core.views.reset_password, name='reset_password'),
    path('admin/', admin.site.urls),
]
