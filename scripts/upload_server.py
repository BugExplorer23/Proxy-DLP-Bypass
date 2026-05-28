import os
import socket
from flask import Flask, request, redirect, url_for, render_template_string

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

HTML_PAGE = """
<!doctype html>
<title>File Upload</title>
<h2>Upload a File</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename:
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(save_path)
            return f"File uploaded successfully: {file.filename}"
        return "No file selected"
    return render_template_string(HTML_PAGE)


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    ip = get_local_ip()
    port = 8080
    print(f"\nServer running at: http://{ip}:{port}\n")
    print("Open this URL from any device on the same network.\n")
    app.run(host="0.0.0.0", port=port)
