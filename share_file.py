# save as server.py and run it on your laptop
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = '''
<!doctype html>
<title>Send File to Laptop</title>
<h2>Upload file from your phone</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file><br><br>
  <input type=submit value=Upload>
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        return '✅ File uploaded successfully!'
    return render_template_string(HTML)

if __name__ == '__main__':
    # Replace with your laptop's local IP
    app.run(host='0.0.0.0', port=5000)
