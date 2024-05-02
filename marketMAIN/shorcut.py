from flask import Flask, Blueprint, render_template, request, redirect, url_for

bp = Blueprint('shortcut', __name__, url_prefix='/shortcut')
 
@bp.route('/shortcut')
def shortcut():
    return render_template('shortcut.html')

@bp.route('/settings')
def settings():
    return render_template('settings/settings.html')