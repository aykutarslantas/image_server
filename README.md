
# OCR (Optical Character Recognition) Flask App

This is a simple Flask web application for performing OCR on uploaded images. The application uses the Tesseract OCR engine along with image processing techniques to extract text information from images.

## Usage
1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```
2. Build the Docker image:

```bash
docker-compose build
```

3. Run the Docker container:

```bash
docker-compose up
```

The application will be accessible at http://localhost:5000. You can use any API testing tool or write a simple client to send image files to the /ocr endpoint.

## API Endpoint

- POST /ocr
  -  Accepts an image file via a POST request.
  - Parameters:
    - file: Image file to be processed.
  - Returns JSON response:
    - If successful: {'ocr_result': 'Extracted text'}
    - If an error occurs: {'error': 'Error message'}

## Requirements
Make sure you have Docker installed on your machine.

# Docker Configuration
The Dockerfile uses the official Python 3.8 slim-buster image. It installs the required dependencies from the requirements.txt file and the Tesseract OCR for the Turkish language.

# Dependencies
 - Flask
 - numpy
 - opencv-python-headless
 - Pillow
 - pytesseract

## Note
Ensure that you have the necessary Tesseract language files for Turkish **(tesseract-ocr-tur)** installed on your system.

Feel free to customize the application according to your needs. Happy coding!
