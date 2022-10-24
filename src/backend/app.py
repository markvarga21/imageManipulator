from flask import Flask, request, send_file

from service.retouch_service import get_retouch_image_file, retouch_image_all_in_one
from util.image_converter import convert_string_to_pillow_image
from util.value_mapper import CONTRAST_FRONTEND_MAX, CONTRAST_FRONTEND_MIN, COLOR_FRONTEND_MIN, COLOR_FRONTEND_MAX, \
    SHARPNESS_FRONTEND_MIN, SHARPNESS_FRONTEND_MAX, BLUR_FRONTEND_MIN, BLUR_FRONTEND_MAX

app = Flask(__name__)


@app.route('/getModifiedImageSeparate', methods=['GET', 'POST'])
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


@app.route('/getMaxContrastValue', methods=['GET'])
def get_max_contrast():
    return str(CONTRAST_FRONTEND_MAX)


@app.route('/getMinContrastValue', methods=['GET'])
def get_min_contrast():
    return str(CONTRAST_FRONTEND_MIN)


@app.route('/getMinColorValue', methods=['GET'])
def get_min_color():
    return str(COLOR_FRONTEND_MIN)


@app.route('/getMaxColorValue', methods=['GET'])
def get_max_color():
    return str(COLOR_FRONTEND_MAX)


@app.route('/getMinSharpnessValue', methods=['GET'])
def get_min_sharpness():
    return str(SHARPNESS_FRONTEND_MIN)


@app.route('/getMaxSharpnessValue', methods=['GET'])
def get_max_sharpness():
    return str(SHARPNESS_FRONTEND_MAX)


@app.route('/getMinBlurValue', methods=['GET'])
def get_min_blur():
    return str(BLUR_FRONTEND_MIN)


@app.route('/getMaxBlurValue', methods=['GET'])
def get_max_blur():
    return str(BLUR_FRONTEND_MAX)


@app.route('/getModifiedImageAllInOne', methods=['GET'])
def get_modified_image_all_in_one():
    file_str = request.files['file'].read()
    pillow_img = convert_string_to_pillow_image(file_str)
    retouch_values = {
        'brightness': request.form['brightness'],
        'contrast': request.form['contrast'],
        'color': request.form['color'],
        'sharpness': request.form['sharpness'],
        'blur': request.form['blur']
    }
    retouched_file = retouch_image_all_in_one(pillow_image=pillow_img, values=retouch_values)
    if retouched_file is not None:
        print(retouched_file.name)
        return send_file(retouched_file.name, mimetype='image/jpeg')
    else:
        return 'Image is None!'


if __name__ == '__main__':
    app.run(debug=True)
