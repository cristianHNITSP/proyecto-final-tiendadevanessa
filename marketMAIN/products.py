from flask import Flask, Blueprint, render_template, request, redirect, url_for

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/warehouse')
def warehouse():
    return render_template('products/warehouse.html')

@bp.route('/manage_warehouse')
def managewarehouse():
    return render_template('products/manage-warehouse.html')

@bp.route('/manage_presentation')
def managepresentation():
    return render_template('products/manage-presentation.html')

@bp.route('/manage_sallers')
def managesallers():
    return render_template('products/manage-sallers.html')

@bp.route('/manage_company')
def managecompany():
    return render_template('products/manage-company.html')

