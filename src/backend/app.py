from flask import Flask, request, send_file

from service.retouch_service import get_retouch_image_file
from util.image_converter import convert_string_to_pillow_image

app = Flask(__name__)


@app.route('/getModifiedImage', methods=['GET'])
def get_modified_image():
    file_str = request.files['file'].read()
    pillow_img = convert_string_to_pillow_image(file_str)
    manipulation_type = request.form['type']
    new_value = float(request.form['newValue'])
    retouched_file = get_retouch_image_file(pillow_img, manipulation_type, new_value)
    if retouched_file is not None:
        print(retouched_file.name)
        return send_file(retouched_file.name, mimetype='image/jpeg')
    else:
        return 'Image is None!'


if __name__ == '__main__':
    app.run(debug=True)
