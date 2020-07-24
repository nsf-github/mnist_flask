import base64
import io

from flask import Flask, render_template, request

from tools import image_prepare

app = Flask(__name__, static_url_path='', root_path='/home/nsf/Desktop/workspace/mnist_flask')


@app.route('/')
def login():
    return render_template('html5-canvas-drawing-app.html')


@app.route('/upload_img', methods=['POST'])
def show_time():
    img_b64encode = request.json['img_data'][22:]
    img_b64decode = base64.b64decode(img_b64encode)
    image = io.BytesIO(img_b64decode)
    result = image_prepare(image)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
