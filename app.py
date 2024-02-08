from flask import Flask, render_template, request

app = Flask(__name__)

def convert_currency(amount, base_currency='AUD'):
    # Tasas de cambio ficticias
    exchange_rates = {
        'AUD': 1.0,
        'EUR': 0.61,
        'USD': 0.74,
        'RUB': 71.21,  # ¡Puedes ajustar estas tasas según sea necesario!
    }
    
    converted_values = {currency: round(amount * exchange_rates[currency], 2) for currency in exchange_rates}
    return converted_values

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        converted_values = convert_currency(amount)
        return render_template('index.html', amount=amount, converted_values=converted_values)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

