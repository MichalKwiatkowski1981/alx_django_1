from django.urls import path
from main.views import hello_world, contacts, contacts2, add_post_form, contact

app_name = 'main'
urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('contacts', contacts, name='contacts'),
    path('contacts2', contacts2, name='contacts2'),
    path('contact', contact, name="contact")
]

