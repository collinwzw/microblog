from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect

#In this example there are two decorators, which associate the URLs / and /index to this function. 
#This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response.
@app.route('/') #@app.route decorator creates an association between the URL given as an argument and the function. 
@app.route('/index')
def index():
    user = {'username': 'Ziwen'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)