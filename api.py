from flask import Flask, request, jsonify
import werkzeug
import os
from youtube import video_pred
from image import image_pred
from image_format_conv import check_and_convert_image
app = Flask(__name__)

ALLOWED_VIDEO_EXTENSIONS = {'mp4'}

ALLOWED_IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename, accepted_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in accepted_extensions


@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No selected image file'}), 400

    if not allowed_file(image.filename, ALLOWED_IMAGE_EXTENSIONS):
        return jsonify({'error': 'Invalid image file extension'}), 400

    try:
        # ... (similar to previous code for image processing)
        image_path = werkzeug.utils.secure_filename(image.filename)
        # print(image_path)
        # print(type(image_path))
        image.save(image_path)
        image_path=check_and_convert_image(image_path)
        output_string = image_pred(image_path=image_path)
        return jsonify({'output': output_string}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        # Ensure the temporary video file is deleted
        # if image_path and os.path.exists(image_path):
        os.remove(image_path)
        print()
    

@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400

    video = request.files['video']

    if video.filename == '':
        return jsonify({'error': 'No selected video file'}), 400

    if not allowed_file(video.filename, ALLOWED_VIDEO_EXTENSIONS):
        return jsonify({'error': 'Invalid file extension'}), 400

    try:
        # Store the video temporarily
        video_path = werkzeug.utils.secure_filename(video.filename)
        video.save(video_path)
        ans = video_pred(video_path=video_path)

        return jsonify({'output': ans}), 200

    except Exception as e:
        # Handle any errors during processing
        return jsonify({'error': str(e)}), 500

    finally:
        # Ensure the temporary video file is deleted
        if video_path and os.path.exists(video_path):
            os.remove(video_path)


if __name__ == '__main__':
    app.run(debug=True)