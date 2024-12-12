# URL Scraping Chatbot

This project is a URL scraping chatbot application built with React, Django, and other modern technologies. The chatbot allows users to input a URL, scrape data from the specified website, and interact with a chatbot that provides responses based on the scraped data.

## Technologies Used

1. **React**
   - A JavaScript library for building user interfaces, particularly single-page applications.
  
2. **TypeScript**
   - A superset of JavaScript that adds static typing to the language, enhancing the development experience.

3. **Django**
   - A high-level Python web framework that encourages rapid development and clean, pragmatic design for building web applications.

4. **FastAPI**
   - A modern, fast web framework for building APIs with Python, known for its performance and ease of use.

5. **ChromaDB**
   - A vector database designed for machine learning and AI applications, used for efficient storage and retrieval of data.

6. **Google Gemini API**
   - An AI-powered API from Google for natural language processing and interaction capabilities.

7. **CSS**
   - A stylesheet language used for styling the application.

8. **HTML**
   - The standard markup language for creating web pages, used to define the structure of the application.

9. **JavaScript**
    - The programming language enabling interactive web pages and dynamic functionality.

10. **Fetch API**
    - A modern interface for making HTTP requests in JavaScript, used for communicating with the backend.

11. **npm (Node Package Manager)**
    - A package manager for JavaScript, used to manage project dependencies.

12. **Version Control (e.g., Git)**
    - A system that tracks changes to files over time, allowing for version control and collaboration.

## Installation Instructions

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Node.js** (for the frontend)
- **Python 3.x** (for the backend)
- **pip** (Python package manager)
- **Git** (optional, for version control)

### Cloning the Repository

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yug-sinha/urlbot.git
   cd urlbot
   ```

### Setting Up the Frontend

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install the dependencies using npm:

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```

4. Alternatively, you can start the production build by running:

   ```bash
   npm start
   ```

### Setting Up the Backend

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

### Accessing the Application

Once both the frontend and backend servers are running, open your web browser and navigate to:

```
http://localhost:3000
```

## Usage

1. Enter a URL in the input field and click the "Scrape Website" button to scrape data from the provided URL.
2. After scraping, you can interact with the chatbot by typing messages in the message input field and pressing "Enter" or clicking the "Send" button.

## Video Demonstration

Here’s a video demonstration of the application: 

https://github.com/user-attachments/assets/eb333ed9-2e66-475a-831d-af766dad634a

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the contributors and libraries that made this project possible.
- Inspiration from various resources on web scraping and chatbot development.
```
