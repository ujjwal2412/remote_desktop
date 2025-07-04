# Remote Desktop & File Sharing Over Local Network

A lightweight Python + Flask-based remote desktop controller and file sharing tool built for flexibility, speed, and ease of use over a local network.

## 🔧 Features

### 🎮 Remote Desktop Controls
- Play / Pause media
- Forward / Backward seek (e.g. ±3s, ±10s)
- Volume Up / Down
- Customizable UI and command bindings
- Works over local network (Wi-Fi or hotspot)

### 📂 Local File Sharing
- Share files between devices at full LAN speed (tested up to 50 MBps)
- Simple browser-based interface
- No third-party servers, 100% local and private

## 🚀 Getting Started

### 1. Install Dependencies
pip install flask
2. Run the Server
3. Access the Interface
Open your browser and go to http://<your-laptop-ip>:<port>
(Default port is usually 5000)

Use your phone or another device on the same network to control the desktop or transfer files.

⚙️ Customization
Modify the templates/ folder for UI changes

Commands are handled in app.py – easily extend or change them as needed

📦 Tech Stack
Python

Flask

HTML/CSS/JS

💡 Use Cases
Control media while watching from a distance

Quickly transfer files over local hotspot or Wi-Fi

Create your own remote automation panel

🛡️ Privacy First
All operations are performed locally.

No data leaves your network.

📄 License
MIT License – use it freely, customize it, break it, fix it.