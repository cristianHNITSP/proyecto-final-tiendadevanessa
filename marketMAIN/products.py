from flask import Flask, Blueprint, render_template, request, redirect, url_for

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/viewproduct')
def viewproduct():
    return render_template('products/view-product.html')

@bp.route('/editproduct')
def editproduct():
    return render_template('products/edit-product.html')

@bp.route('/addproduct')
def addproduct():
    return render_template('products/add-product.html')

