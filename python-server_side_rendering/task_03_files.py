from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
