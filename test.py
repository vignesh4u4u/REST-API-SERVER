from currency_converter import CurrencyConverter
from flask import Flask,request,jsonify
from gevent.pywsgi import WSGIServer
app = Flask(__name__)

def convert_to_sgd(amount, from_currency):
    c = CurrencyConverter()
    try:
        converted_amount = c.convert(amount, from_currency.upper(), 'SGD')
        return converted_amount
    except Exception as e:
        return f"Error: {e}"
@app.route("/currency_conversion",methods=["POST"])
def conversion():
    try:
        input_string = request.form["currency"]
        numeric_part = ""
        alphabetic_part = ""
        for char in input_string:
            if char.isdigit():
                numeric_part += char
            elif char.isalpha():
                alphabetic_part += char
        converted_amount = convert_to_sgd(numeric_part, alphabetic_part)
        return jsonify({
            "status": "success",
            "SGD_AMOUNT":converted_amount
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    print("Starting the server on port 8080")
    #flask_app.run(debug=False, host="0.0.0.0", port=8080)
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    print('Server running on http://0.0.0.0:8080')
    http_server.serve_forever()