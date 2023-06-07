from flask import Flask, session, render_template, request, redirect, g, url_for

app = Flask(__name__)

app.secret_key = '123456789'

@app.route('/')
def homepage():
    return render_template('/home.html')

@app.route('/login')
def loginpage():
    return render_template('login.html', errou=0)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('usuario', None)
        if request.form['senha'] == '123456':
            session['usuario'] = request.form['usuario']
            return redirect(url_for('menuprincipal'))

    return render_template('login.html', errou=1)

@app.route('/menuprincipal')
def menuprincipal():
    if g.usuario:
        return render_template('menuprincipal.html',usuario=session['usuario'])
    return redirect(url_for('login'), errou=0)

@app.before_request
def before_request():
    g.usuario = None
    if 'usuario' in session:
        g.usuario = session['usuario']

@app.route('/dropsession')
def dropsession():
    session.pop('usuario', None)
    return render_template('/login.html', errou=0)

if __name__ == '__main__':
    app.run(debug=True)
