from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests
import google.generativeai as genai

# Configure the Google AI SDK with your API key directly
GEMINI_API_KEY = "YOUR_API_KEY"  # Update with your specified key
genai.configure(api_key=GEMINI_API_KEY)

# Dictionary to hold the scraped data temporarily
scraped_data = {}

@api_view(['POST'])
def scrape_website(request):
    url = request.data.get('url')
    if not url:
        return Response({"error": "No URL provided"}, status=400)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=400)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Scrape the title and all paragraphs for a more comprehensive view
    title = soup.title.string if soup.title else "No title found"
    paragraphs = soup.find_all('p')

    # Extract text from all paragraphs and join them
    content = ' '.join([para.text for para in paragraphs])

    # Store the scraped data
    scraped_data['title'] = title
    scraped_data['content'] = content

    # Debugging output to verify the scraped data
    print("Scraped Data:", scraped_data)

    return Response({"title": title, "content": content}, status=200)

@api_view(['POST'])
def chatbot_prompt(request):
    user_input = request.data.get('input')
    if not user_input:
        return Response({"error": "No input provided"}, status=400)

    # Check if there is scraped content available
    if 'content' in scraped_data and 'title' in scraped_data:
        # Prepare the prompt for the Gemini model using scraped content
        prompt = f"Here's what I found about {scraped_data['title']}:\n{scraped_data['content']}\n\nUser asked: {user_input}"
    else:
        return Response({"error": "No scraped content available"}, status=400)

    try:
        # Create the model configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",  # Use the correct model name
            generation_config=generation_config
        )

        # Start the chat session
        chat_session = model.start_chat(history=[])

        # Send the prepared prompt as a message
        response = chat_session.send_message(prompt)
        
        # Extract the response text
        response_text = response.text if response else 'No response from API'
        
    except Exception as e:
        return Response({"error": str(e)}, status=400)

    return Response({"response": response_text}, status=200)
