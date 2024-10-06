# chatbot/urls.py

from django.urls import path
from .views import chatbot_prompt  # Adjust the import as necessary

urlpatterns = [
    path('', chatbot_prompt, name='chatbot_prompt'),  # Make sure this matches what you expect
]
