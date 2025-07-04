from flask import Flask, request, send_from_directory, render_template
import os
import time

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
@app.route('/upload', methods=['POST'])
def upload():
    start_time = time.time()
    files = request.files.getlist('file')
    uploaded = []

    for f in files:
        if f.filename:
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(save_path)
            uploaded.append(f.filename)

    duration = round(time.time() - start_time, 2)
    return {'success': True, 'filenames': uploaded, 'time': duration}


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
