from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform login validation here
        # For example, check if the credentials are valid

        if username == 'admin' and password == 'password':
            return redirect(url_for('buttons'))
        else:
            return 'Invalid credentials'

    return render_template('login.html')


@app.route('/buttons')
def buttons():
    return render_template('buttons.html')


@app.route('/buttons1')
def buttons1():
    return render_template('buttons1.html')

@app.route('/buttons2')
def buttons2():
    return render_template('buttons2.html')

@app.route('/buttons3')
def buttons3():
    return render_template('buttons3.html')



if __name__ == '__main__':
    app.run(debug=True)
