# victim_server.py (Flask)
from flask import Flask, request, render_template_string, redirect, make_response

app = Flask(__name__)

user_email = "victim@example.com"

@app.route('/')
def index():
    return f"<h1>Welcome! Your email is: {user_email}</h1><a href='/change'>Change Email</a>"

@app.route('/change', methods=['GET', 'POST'])
def change_email():
    global user_email
    if request.method == 'POST':
        new_email = request.form.get('email')
        user_email = new_email
        return redirect('/')
    return '''
        <form method="POST" action="/change">
            New Email: <input type="email" name="email" value="victim@example.com">
            <input type="submit" value="Change">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
