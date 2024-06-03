from flask import request, jsonify, Blueprint
import requests

# External API endpoint for fetching live exchange rates
EXCHANGE_RATE_API_URL = "https://open.er-api.com/v6/latest/USD"

convertRoute = Blueprint("convert", __name__)


@convertRoute.route("/", methods=["GET"])
def convert_currency():
    source_currency = request.args.get("from")
    target_currency = request.args.get("to")
    amount = float(request.args.get("amount"))

    # Fetch current rates from the external API
    response = requests.get(EXCHANGE_RATE_API_URL)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exchange rates"}), 500

    exchange_rates = response.json()["rates"]

    if source_currency != "USD":
        amount = amount / exchange_rates[source_currency]

    converted_amount = amount * exchange_rates[target_currency]

    return jsonify(
        {
            "source_currency": source_currency,
            "target_currency": target_currency,
            "amount": request.args.get("amount"),
            "converted_amount": converted_amount,
        }
    )