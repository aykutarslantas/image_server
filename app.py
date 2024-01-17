from flask import Flask, request, jsonify
import cv2
import numpy as np
import pytesseract
from PIL import Image

app = Flask(__name__)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def noise_removal(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return image

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Görüntüyü oku ve işle
        image = Image.open(file.stream)
        image = np.array(image)
        gray_image = grayscale(image)
        thresh, im_bw = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        no_noise = noise_removal(im_bw)
        ocr_result = pytesseract.image_to_string(no_noise, lang='tur')

        return jsonify({'ocr_result': ocr_result})

    return jsonify({'error': 'An error occurred during file processing'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)