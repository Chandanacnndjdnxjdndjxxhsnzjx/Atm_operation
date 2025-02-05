from flask import Flask, render_template, request

app = Flask(__name__)

# Initial ATM data
ATM_PIN = "5693"
account_balance = 10000

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/validate', methods=['POST'])
def validate():
    user_pin = request.form.get("pin")
    if user_pin == ATM_PIN:
        return render_template("menu.html", balance=account_balance)
    else:
        return "Invalid PIN. Please try again. <a href='/'>Go Back</a>"

@app.route('/transaction', methods=['POST'])
def transaction():
    global account_balance
    action = request.form.get("action")
    
    if action == "balance":
        return f"Your account balance is: {account_balance} <a href='/'>Go Back</a>"
    
    elif action == "withdraw":
        withdraw_amount = int(request.form.get("amount"))
        if withdraw_amount <= account_balance:
            account_balance -= withdraw_amount
            return f"Withdrawal successful! Amount withdrawn: {withdraw_amount}. Remaining balance: {account_balance} <a href='/'>Go Back</a>"
        else:
            return "Insufficient balance. <a href='/'>Go Back</a>"
    
    elif action == "deposit":
        deposit_amount = int(request.form.get("amount"))
        account_balance += deposit_amount
        return f"Deposit successful! Updated balance: {account_balance} <a href='/'>Go Back</a>"
    
    return "Invalid action. <a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)
