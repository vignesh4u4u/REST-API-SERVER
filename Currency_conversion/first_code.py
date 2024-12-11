from currency_converter import CurrencyConverter
from flask import request,Flask,jsonify
from gevent.pywsgi import WSGIServer
app = Flask(__name__)
def convert_to_sgd(amount, from_currency):
    c = CurrencyConverter()

    try:
        converted_amount = c.convert(amount, from_currency.upper(), 'SGD')
        return converted_amount
    except Exception as e:
        return f"Error: {e}"

@app.route("/currency",methods=["POST"])
def amount_conversion_sgd():
    try:
        amount = request.form["amount"]
        from_currency = request.form["from_currency"]
        converted_amount = convert_to_sgd(amount, from_currency.upper())
        return jsonify({"message":f"{amount} {from_currency.upper()} is equal to {converted_amount:.5f} SGD"})
    except Exception as e:
        return jsonify({"Error":"This format currency can't converted"})

if __name__ == "__main__":
    print("Starting the server on port 8080")
    #flask_app.run(debug=False, host="0.0.0.0", port=8080)
    http_server = WSGIServer(('0.0.0.0', 8080), app)
    print('Server running on http://0.0.0.0:8080')
    http_server.serve_forever()



