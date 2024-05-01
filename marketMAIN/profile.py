from flask import Flask, Blueprint, render_template, request, redirect, url_for

bp = Blueprint('profile', __name__, url_prefix='/profile')
 
@bp.route('/welcomeuser')
def welcomeuser():
    return render_template('profile/welcome-user.html')

@bp.route('/profile')
def profile():
    return render_template('profile/profile.html')


