from flask import Flask, Blueprint, render_template, request, redirect, url_for

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/warehouse')
def warehouse():
    return render_template('products/warehouse.html')


@bp.route('/Manage_warehouse')
def managewarehouse():
    return render_template('products/Manage-warehouse.html')
