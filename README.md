# Language Translation Workspace

This project is a simple web application for translating text using a translation API. It is built with Flask and provides a user-friendly interface for inputting text and selecting the target language for translation.

## Project Structure

```
language-translation-workspace
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   └── translation_model.py
│   ├── routes
│   │   └── translate.py
│   └── templates
│       └── index.html
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd language-translation-workspace
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can start the Flask application by running:
   ```
   python app/main.py
   ```
   The application will be accessible at `http://localhost:5000`.

## Docker Instructions

To run the application using Docker, follow these steps:

1. **Build the Docker image:**
   ```
   docker build -t language-translation-app .
   ```

2. **Run the Docker container:**
   ```
   docker run -p 5000:5000 language-translation-app
   ```
   The application will be accessible at `http://localhost:5000`.

## Usage

- Open your web browser and navigate to `http://localhost:5000`.
- Enter the text you want to translate and select the target language.
- Click the "Translate" button to see the translated text displayed on the page.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.