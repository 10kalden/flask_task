from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        reenter_password = request.form['reenter_password']

        return redirect(url_for('home'))

    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
