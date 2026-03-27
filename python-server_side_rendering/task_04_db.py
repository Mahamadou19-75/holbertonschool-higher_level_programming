from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON
def read_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

# CSV
def read_csv():
    data = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception:
        return []
    return data

# SQLITE
def read_sqlite():
    data = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        for row in rows:
            data.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()
    except Exception:
        return []
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Vérifier source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Charger data
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        products = read_sqlite()

    # Filtre ID
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if int(p.get('id')) == product_id]
        except Exception:
            products = []

        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)