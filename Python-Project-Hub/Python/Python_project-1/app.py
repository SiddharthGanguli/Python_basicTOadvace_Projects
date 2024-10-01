from flask import Flask, render_template, request

app = Flask(__name__)

# Menu dictionary
menu = {
    "Pasta": 150,
    "Pizza": 200,
    "Burger": 250,
    "Coffee": 50,
    "Salad": 70
}

# Global bill tracker
total_bill = 0

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML template (frontend)

@app.route('/order', methods=['POST'])
def order():
    global total_bill
    item1 = request.form['item1'].capitalize()  # Get the item from form input

    if item1 in menu:
        price = menu[item1]
        total_bill += price
        return f"Your order for {item1} is successful! Price: ₹ {price}. Total Bill: ₹ {total_bill}. <br><a href='/'>Order More</a>"
    else:
        return f"Sorry, {item1} is not available. <br><a href='/'>Order Again</a>"

if __name__ == '__main__':
    app.run(debug=True)
