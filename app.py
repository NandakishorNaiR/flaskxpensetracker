from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

categories = ["Food", "Transport", "Entertainment", "others"]
expenses = {category: 0.0 for category in categories}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form.get('category')
        amount = request.form.get('amount')

        if category and amount and category in expenses and amount.isnumeric():
            expenses[category] += float(amount)

            return redirect(url_for('index'))

        total_expenses = sum(expenses.values())

        summary = {
            category: {'amount': amount, 'percentage': (amount / total_expenses) * 100 if total_expenses > 0 else 0}
            for category, amount in expenses.items()}
        print("Summary: ", summary)
        print("Total Expenses: ", total_expenses)
        print("Categories: ", categories)

        return render_template('index.html', expenses=summary, total=total_expenses, categories=categories)

    if __name__ == '__main__':
        print("Starting the Flask server on http://127.0.0.1:5000")
        app.run(debug=True, port=5000)


