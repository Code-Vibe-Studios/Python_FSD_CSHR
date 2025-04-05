from flask import Flask, render_template, request, flash, redirect, url_for,session

app = Flask(__name__)
app.secret_key ="secret"

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/jinja')
def jinja():
    name = input("Enter the Name: ")
    return render_template('jinja.html',username=name)

@app.route('/api/v1', methods=['GET','POST'])
def apiV1():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}"
    return render_template('apiV1.html')

@app.route('/api/v2',methods=['GET','POST'])
def apiV2():
    if request.method == 'POST':
        username = request.form['name']
        flash(f"Hello, {username}! Your data has been saved.","success")
        # return redirect(url_for('apiV1'))
    return render_template('apiV2.html')


@app.route('/v1/')
def homeV1():
    username = session.get('username')
    return render_template('home.html',username=username)

@app.route('/v1/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('homeV1'))
    return render_template('login.html')

@app.route('/v1/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('homeV1'))

if __name__ == '__main__':
    app.run(debug=True)