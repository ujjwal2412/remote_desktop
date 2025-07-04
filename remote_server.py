from flask import Flask, render_template, request
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    action = request.form.get('action')
    
    if action == 'pause':
        pyautogui.press('space')
    elif action == 'rewind_3':
        pyautogui.hotkey('shift', 'left')
    elif action == 'forward_3':
        pyautogui.hotkey('shift', 'right')
    elif action == 'rewind_10':
        pyautogui.press('left')
    elif action == 'forward_10':
        pyautogui.press('right')

    return '', 204  # No content response

app.run(host='0.0.0.0', port=8000)
