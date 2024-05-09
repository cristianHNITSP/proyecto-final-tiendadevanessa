from flask import Flask, Blueprint, render_template, request, redirect, url_for


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect(url_for('auth.signin'))
    return render_template('auth/signup.html', )

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        return redirect(url_for('profile.welcomeuser'))
    return render_template('auth/signin.html')