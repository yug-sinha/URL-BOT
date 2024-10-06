# scraping/urls.py

from django.urls import path, include
from chatbot.views import scrape_website, chatbot_prompt

urlpatterns = [
    path('api/scrape/', scrape_website, name='scrape'),
    path('api/chatbot/', chatbot_prompt, name='chatbot_prompt'),
]

# If you have a separate urls.py in the chatbot folder, you can include it like this:
# path('chatbot/', include('chatbot.urls')),
