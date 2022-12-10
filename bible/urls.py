from django.contrib import admin
from django.urls import path

import bible.core.views

urlpatterns = [
    path('', bible.core.views.home, name='home'),
    path('sign-in/', bible.core.views.sign_in, name='sign-in'),
    path('sign-up/', bible.core.views.sign_up, name='sign-up'),
    path('sign-out/', bible.core.views.sign_out, name='sign-out'),
    path('reset-password/', bible.core.views.reset_password, name='reset-password'),
    path('admin/', admin.site.urls),
]
