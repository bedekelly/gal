import os
import re
import sys
from io import BytesIO
from base64 import b64encode
from functools import lru_cache

from flask import Flask, render_template, jsonify, send_from_directory
from PIL import Image, ImageFilter

from config import PREVIEW_SIZE, BLUR_RADIUS, IMAGE_FOLDER

app = Flask(__name__)


def is_image(filename):
    return re.match("^.*\.(jpg|png|jpeg)$", filename)


def data_url(image_bytes):
    raw_bytes = image_bytes.getvalue()
    return 'data:image/webp;base64,' + b64encode(raw_bytes).decode("utf-8")


def thumbnail_of(image_filename):
    filepath = os.path.join(IMAGE_FOLDER, image_filename)
    image = Image.open(filepath)
    image.thumbnail(PREVIEW_SIZE)
    return image


def blurred(image):
    image_output = BytesIO()
    blurred = image.filter(ImageFilter.GaussianBlur(radius=BLUR_RADIUS))
    blurred.save(image_output, "WEBP")
    return image_output


@lru_cache(1024)
def preview_of(image, number, total):
    # It's important to thumbnail, *then* blur to keep things speedy!
    print(f" Image preview [{number+1}/{total}]")
    thumbnail = thumbnail_of(image)
    blurred_thumbnail = blurred(thumbnail)
    return data_url(blurred_thumbnail)


def local_images():
    working_dir = os.getcwd()
    files = os.listdir(working_dir)
    return [file for file in files if is_image(file)]
    

def generate_previews():
    images = local_images()
    total = len(images)
    return {"images": [
        (image, preview_of(image, num, total)) 
        for num, image in enumerate(images)
    ]}


@app.route("/image/<path>")
def send_image(path):
    return send_from_directory(os.getcwd(), path)


@app.route("/")
def index():
    images = generate_previews()
    return render_template("index.html", json_data=images)


@app.route("/js/<path>")
def static_js(path):
    return send_from_directory("frontend/dist", path)


if __name__ == "__main__":
    IMAGE_FOLDER = sys.argv[1] if len(sys.argv) > 1 else "."
    print("Loading image previews...")
    generate_previews()
    print("Done! Running app on port 5000.")
    app.run(host="0.0.0.0", port=5000)
