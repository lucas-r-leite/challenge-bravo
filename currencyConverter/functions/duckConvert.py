import requests
import json
import re


def duckConvert(source, target, amount):
    source = source.lower()
    target = target.lower()

    url = f"https://duckduckgo.com/js/spice/cryptocurrency/{
        source}/{target}/{amount}"

    headers = {
        "Accept": "*/*",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # print("Response text:", response.text)

        # Extract the JSON part from the response text
        match = re.search(r"\((.*)\)", response.text, re.DOTALL)
        if match:
            json_response = match.group(1)
            data = json.loads(json_response)

            # Extract the first key from the quote dictionary
            quote_keys = list(data["data"]["quote"].keys())
            quoteID = quote_keys[0]

            # Extract the price value
            price = data["data"]["quote"][quoteID]["price"]

            return price
        else:
            print("No match found in the response text")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


if __name__ == "__main__":
    duckConvert("USD", "BRL", 1)