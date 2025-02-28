# app.py - Main Application File

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import os
# import logging_config
# import logging 
from urllib.parse import quote_plus
from datetime import datetime
from markupsafe import Markup


# Initialize App 
app = Flask(__name__)
app.secret_key = 'your_secret_key'
# Main code
#logging.info('Application started.')

# URL encode the password
password = quote_plus('jroshan@98')

#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-testing')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql://root:{password}@localhost/product_db')

# MySQL Configuration with properly encoded password
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{password}@localhost/product_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    create_at = db.Column(db.DateTime, nullable=False)
    update_at = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'<Product {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'create_at': self.create_at,
            'update_at': self.update_at
        }
        
# with app.app_context():
#     db.create_all()
    
# Product Form
class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    quantity = FloatField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')
    
# Routes
@app.route('/')
def index():
    """Display all products"""
    products = Product.query.all()
    # return jsonify(products)
    
    return render_template('index.html', products=products)

@app.route('/product/new_product', methods=['GET', 'POST'])
def create_new_product():
    """Add a new product"""
    form = ProductForm()

    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            quantity=form.quantity.data,
            create_at=datetime.now(),
            update_at=datetime.now()
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully', 'success')
        return redirect(url_for('index'))
    
    return render_template('product_form.html', form=form, title='Add New Product')
@app.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    """Edit an existing product"""
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('index'))
    
    return render_template('product_form.html', form=form, title='Edit Product')

@app.route('/product/<int:product_id>/delete', methods=['POST'])
def delete_product(product_id):
    """Delete a product"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('index'))

# API Routes for AJAX operations
@app.route('/api/products', methods=['GET'])
def get_products():
    """API to get all products"""
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """API to get a specific product"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

@app.route('/api/products', methods=['POST'])
def api_create_product():
    """API to create a product"""
    data = request.json
    
    if not all(k in data for k in ('name', 'price', 'quantity')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        quantity=data['quantity']
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify(product.to_dict()), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def api_update_product(product_id):
    """API to update a product"""
    product = Product.query.get_or_404(product_id)
    data = request.json
    
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'quantity' in data:
        product.quantity = data['quantity']
    
    db.session.commit()
    
    return jsonify(product.to_dict())

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def api_delete_product(product_id):
    """API to delete a product"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'})

# main functions 
if __name__=='__main__':
    #logging.info('Starting Main Function.')
    app.run(debug=True,port='5000',host='0.0.0.0')
