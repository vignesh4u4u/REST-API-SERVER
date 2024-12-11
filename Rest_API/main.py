from flask import Flask,request
from gevent.pywsgi import WSGIServer
from Rest_API.sample import image_to_text
app = Flask(__name__)
@app.route('/generate', methods=['POST'])
def ocr():
    files = request.files.getlist("file")
    output_answer = image_to_text(files)
    return output_answer

if __name__ == "__main__":
    print("Starting the server on port 8080")
    #app.run(debug=False, host="0.0.0.0", port=8080)
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    print('Server running on http://0.0.0.0:8080')
    http_server.serve_forever()


