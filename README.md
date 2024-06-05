# Flask Currency Converter

This is a simple Flask application that converts currency using data from DuckDuckGo's cryptocurrency API.

## Setup

1. Clone repository:

```git
git clone <repository_url>
```

2. Change directory to the project folder:

```bash
cd <project_folder>
```

3. Create virtual environment:

```python
python3 -m venv venv
```

4. Activate virtual environment:

- On Windows:

    ```bash
    venv\Scripts\activate
    ```

- On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install the required packages:

```python
pip install -r requirements.txt
```

6. Run the Flask app:

```python
python app.py
```

## Or use Docker

1. Build image: `docker build -t <image_name> .`
2. Run the image: `docker run -p 5000:5000 <image_name>`

## Usage

To use the currency converter API, send a GET request to the root endpoint with the following query parameters:

- from: The source currency code (e.g., USD).
- to: The target currency code (e.g., BRL).
- amount: The amount to convert.

Example:

```vbnet
GET http://127.0.0.1:5000/?from=USD&to=BRL&amount=1
```
