from flask import request, jsonify, Blueprint
from functions.duckConvert import duckConvert


convertRoute = Blueprint("convert", __name__)


@convertRoute.route("/", methods=["GET"])
def convert_currency():
    source_currency = request.args.get("from")
    target_currency = request.args.get("to")
    amount = float(request.args.get("amount"))

    converted_amount = duckConvert(source_currency, target_currency, amount)

    return jsonify(
        {
            "source_currency": source_currency,
            "target_currency": target_currency,
            "amount": request.args.get("amount"),
            "converted_amount": converted_amount,
        }
    )
