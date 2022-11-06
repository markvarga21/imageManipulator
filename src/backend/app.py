import os

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS, cross_origin
from service.background_remove_service import remove_green_background

from service.login_service import register_user_in_service, log_in_user_in_service, logout_user_in_service
from service.ocr_service import return_extracted_text_for_image, save_pdf_for_cv2_image, save_text_for_cv2_image, \
    save_doc_for_cv2_image
from service.preset_service import save_user_preset, get_presets_for_user_in_service, get_preset_for_user_in_service
from service.retouch_service import get_retouch_image_file, retouch_image_all_in_one
from util.mapping.image_converter import convert_string_to_pillow_image, convert_string_to_cv2_image
from util.mapping.value_mapper import CONTRAST_FRONTEND_MAX, CONTRAST_FRONTEND_MIN, COLOR_FRONTEND_MIN, COLOR_FRONTEND_MAX, \
    SHARPNESS_FRONTEND_MIN, SHARPNESS_FRONTEND_MAX, BLUR_FRONTEND_MIN, BLUR_FRONTEND_MAX

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/getModifiedImageSeparate', methods=['GET'])
def get_modified_image():
    file_str = request.files['file'].read()
    pillow_img = convert_string_to_pillow_image(file_str)
    manipulation_type = request.form['type']
    new_value = float(request.form['newValue'])
    user_name = request.form['userName']
    relative_path = get_retouch_image_file(
        pillow_img, manipulation_type, new_value, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), relative_path)
    return send_file(absolute_path, mimetype='image/jpeg')


@cross_origin()
@app.route('/getModifiedImageAllInOne', methods=['GET'])
def get_modified_image_all_in_one():
    file_str = request.files['file'].read()
    user_name = str(request.form['userName'])
    pillow_img = convert_string_to_pillow_image(file_str)
    retouch_values = {
        'brightness': request.form['brightness'],
        'contrast': request.form['contrast'],
        'color': request.form['color'],
        'sharpness': request.form['sharpness'],
        'blur': request.form['blur']
    }
    relative_path = retouch_image_all_in_one(
        pillow_image=pillow_img, values=retouch_values, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), relative_path)
    return send_file(absolute_path, mimetype='image/jpeg')


@cross_origin()
@app.route('/getMaxContrastValue', methods=['GET'])
def get_max_contrast():
    return str(CONTRAST_FRONTEND_MAX)


@cross_origin()
@app.route('/getMinContrastValue', methods=['GET'])
def get_min_contrast():
    return str(CONTRAST_FRONTEND_MIN)


@cross_origin()
@app.route('/getMinColorValue', methods=['GET'])
def get_min_color():
    return str(COLOR_FRONTEND_MIN)


@cross_origin()
@app.route('/getMaxColorValue', methods=['GET'])
def get_max_color():
    return str(COLOR_FRONTEND_MAX)


@cross_origin()
@app.route('/getMinSharpnessValue', methods=['GET'])
def get_min_sharpness():
    return str(SHARPNESS_FRONTEND_MIN)


@cross_origin()
@app.route('/getMaxSharpnessValue', methods=['GET'])
def get_max_sharpness():
    return str(SHARPNESS_FRONTEND_MAX)


@cross_origin()
@app.route('/getMinBlurValue', methods=['GET'])
def get_min_blur():
    return str(BLUR_FRONTEND_MIN)


@cross_origin()
@app.route('/getMaxBlurValue', methods=['GET'])
def get_max_blur():
    return str(BLUR_FRONTEND_MAX)


@cross_origin()
@app.route('/registerUser', methods=['POST'])
def register_user():
    args = request.args
    args_dict = args.to_dict()
    return register_user_in_service(args_dict)


@cross_origin()
@app.route('/loginUser', methods=['POST'])
def login_user():
    args = request.args
    args_dict = args.to_dict()
    return log_in_user_in_service(args_dict)


@cross_origin()
@app.route('/logoutUser', methods=['DELETE'])
def logout_user():
    args = request.args
    args_dict = args.to_dict()
    return logout_user_in_service(args_dict)


@cross_origin()
@app.route('/savePreset', methods=['POST'])
def save_preset():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        return save_user_preset(json)
    return 'Content-Type application/json not supported!'


@cross_origin()
@app.route('/getPresets', methods=['GET'])
def get_presets_for_user():
    d = request.args
    preset_dict = get_presets_for_user_in_service(d)
    return jsonify(preset_dict)


@cross_origin()
@app.route('/getPreset', methods=['GET'])
def get_preset_for_user_and_preset_name():
    d = request.args
    preset_dict = get_preset_for_user_in_service(d)
    return jsonify(preset_dict)


@cross_origin()
@app.route('/getTextFromImage', methods=['GET'])
def get_text_from_image():
    file_str = request.files['file'].read()
    cv2_img = convert_string_to_cv2_image(file_str)
    text_from_img = return_extracted_text_for_image(cv2_img)
    return text_from_img


@cross_origin()
@app.route('/getPdfFileFromImage', methods=['GET'])
def get_pdf_from_image():
    file_str = request.files['file'].read()
    size = int(request.form['size'])
    r, g, b = int(request.form['r']), int(
        request.form['g']), int(request.form['b'])
    user_name = request.form['userName']
    cv2_img = convert_string_to_cv2_image(file_str)
    relative_path = save_pdf_for_cv2_image(
        cv2_img=cv2_img, r=r, g=g, b=b, size=size, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), relative_path)
    return send_file(absolute_path, mimetype='application/pdf')


@cross_origin()
@app.route('/getTxtFileFromImage', methods=['GET'])
def get_text_file_from_image():
    file_str = request.files['file'].read()
    user_name = str(request.form['userName'])
    cv2_img = convert_string_to_cv2_image(file_str)
    relative_path = save_text_for_cv2_image(cv2_img, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), relative_path)
    return send_file(absolute_path, mimetype='text/plain')


@cross_origin()
@app.route('/getDocFileFromImage', methods=['GET'])
def get_doc_file_from_image():
    file_str = request.files['file'].read()
    font_size = int(request.form['size'])
    user_name = str(request.form['userName'])
    cv2_img = convert_string_to_cv2_image(file_str)
    relative_path = save_doc_for_cv2_image(
        cv2_img=cv2_img, font_size=font_size, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), relative_path)
    return send_file(absolute_path, mimetype='application/msword')


@cross_origin()
@app.route('/getPngFromImage', methods=['GET'])
def get_png():
    file_str = request.files['file'].read()
    user_name = str(request.form['userName'])
    cv2_img = convert_string_to_cv2_image(file_str)
    relative_path = remove_green_background(
        cv2_img=cv2_img, user_name=user_name)
    absolute_path = os.path.join(os.getcwd(), relative_path)
    return send_file(absolute_path, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
