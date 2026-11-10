from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    home_url = url_for('home')
    return render_template('about.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html')

@app.route('/users/')
def user_list():
    users = [
    {
        "name":"John Doe",
        "email": 'johndoe@gmail.com',
        "password": 123456
    },
    {
        "name":"Smith Adams",
        "email": 'smithadams@gmail.com',
        "password": 123456
    },

    {
        "name":"Williams Gerald",
        "email": 'williamsgerald@gmail.com',
        "password": 123456
    }
]

    return render_template('userList.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)