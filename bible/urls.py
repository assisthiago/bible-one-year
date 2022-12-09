from django.contrib import admin
from django.urls import path

import bible.core.views

urlpatterns = [
    path('sign-in', bible.core.views.sign_in, name='sign-in'),
    path('home', bible.core.views.home, name='home'),
    path('admin/', admin.site.urls),
]
