from flask import Flask, request, send_file, jsonify

from service.login_service import register_user_in_service, log_in_user_in_service, logout_user_in_service
from service.ocr_service import return_extracted_text_for_image
from service.preset_service import save_user_preset, get_presets_for_user_in_service, get_preset_for_user_in_service
from service.retouch_service import get_retouch_image_file, retouch_image_all_in_one
from util.mapping.image_converter import convert_string_to_pillow_image, convert_string_to_cv2_image
from util.mapping.value_mapper import CONTRAST_FRONTEND_MAX, CONTRAST_FRONTEND_MIN, COLOR_FRONTEND_MIN, COLOR_FRONTEND_MAX, \
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
        app.logger.debug(f'File name: {retouched_file.name}')
        return send_file(retouched_file.name, mimetype='image/jpeg')
    else:
        return 'Image is None!'


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
        app.logger.debug(f'File name: {retouched_file.name}')
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


@app.route('/registerUser', methods=['POST'])
def register_user():
    args = request.args
    args_dict = args.to_dict()
    return register_user_in_service(args_dict)


@app.route('/loginUser', methods=['POST'])
def login_user():
    args = request.args
    args_dict = args.to_dict()
    return log_in_user_in_service(args_dict)


@app.route('/logoutUser', methods=['DELETE'])
def logout_user():
    args = request.args
    args_dict = args.to_dict()
    return logout_user_in_service(args_dict)


@app.route('/savePreset', methods=['POST'])
def save_preset():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        return save_user_preset(json)
    return 'Content-Type application/json not supported!'


@app.route('/getPresets', methods=['GET'])
def get_presets_for_user():
    d = request.args
    preset_dict = get_presets_for_user_in_service(d)
    return jsonify(preset_dict)


@app.route('/getPreset', methods=['GET'])
def get_preset_for_user_and_preset_name():
    d = request.args
    preset_dict = get_preset_for_user_in_service(d)
    return jsonify(preset_dict)


@app.route('/getTxtFromImage', methods=['GET'])
def get_pdf_from_image():
    file_str = request.files['file'].read()
    cv2_img = convert_string_to_cv2_image(file_str)
    text_from_img = return_extracted_text_for_image(cv2_img)
    return text_from_img


if __name__ == '__main__':
    app.run(debug=True)
