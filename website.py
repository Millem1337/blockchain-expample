from blockchain import transactions, user
from flask.app import Flask
from flask import render_template, request, session, Flask, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = "8g0hBa59Wmsh2MS"

@app.route('/', methods=["POST", "GET"])
def main_page():
    if 'name' not in session:
        return render_template('main.html', text="Login")
    else:
        return render_template('main.html', text="Profile")

@app.route('/login', methods=["POST", "GET"])
def login_page():
    if 'name' in session:
        return redirect('/profile')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        surname = request.form['surname']
        if user.users.is_user_exists(username) == True:
            session['name'] = username
            session['password'] = password
            session['surname'] = surname
            return redirect('/profile')
        else:
            return redirect('/register')
    else:
        return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register_page():
    if request.method == "POST":
        username = request.form['username']
        surname = request.form['surname']
        password = request.form['password']
        if user.users.is_user_exists(username) == True:
            return render_template('register.html', error="That user is arledly exists!")
        user.users.create_user(username ,surname ,password)
        session['name'] = username
        session['surname'] = surname
        session['password'] = password
        return redirect('/profile')
    else:
        return render_template('register.html')

@app.route('/logout')
def logout_redirect():
    if 'name' in session:
        session['name'] = None
        session['password'] = None
        session['surname'] = None
        return redirect('/')
    else:
        return redirect('/')


@app.route('/profile', methods=["POST", "GET"])
def profile_page():
    if 'name' in session:
        username = session['name']
        surname = session['surname']
        password = session['password']
        uid=user.users.get_id(username)
        return render_template('profile.html', username=username,surname=surname, wallet=user.users.get_wallet(uid), id=uid,transactions=transactions.transactions.get_user_transactions(uid))
    else:
        return redirect('/login')

@app.route('/transaction', methods=["POST", "GET"])
def transaction_form():
    if request.method == "POST":
        if 'name' in session:
            username = request.form['username']
            amount = request.form['amount']
            if amount == None or amount == 0:
                return render_template('transaction_form.html', successfylly="", error="Amount less then 0")
            if user.users.is_user_exists(username) == True:
                Touid = user.users.get_id(username)
                uid = user.users.get_id(session['name'])
                
                transactions.transactions.create_transaction(user.users.get_id(username), user.users.get_id(session['name']), amount)
                if int(amount) >= int(user.users.get_wallet(uid)):
                    return render_template('transaction_form.html', successfylly="", error="Not enough money")
                else:
                    user.users.wallet_add(amount,Touid)
                    user.users.wallet_remove(amount, uid)
                    return render_template('transaction_form.html', successfylly="Successfylly", error="")
            else:
                return render_template('transaction_form.html', successfylly="", error="User not found")
        else:
            return redirect("/")
    else:
        return render_template('transaction_form.html',successfylly="", error="")

@app.route('/addwallet/<amount>')
def addwallet(amount: int):
    if user.users.get_id(session['name']) == 1:
        user.users.wallet_add(amount, user.users.get_id(session['name']))
        return redirect('/profile')
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
