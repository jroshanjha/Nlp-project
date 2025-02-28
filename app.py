from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import logging
import logging_config
import secrets
import string
        
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Main code
logging.info('Application started.')

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jroshan@98'
app.config['MYSQL_DB'] = 'product_db'

mysql = MySQL(app)

# Home Page - Show Products with Search and Pagination
@app.route('/')
def index():
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    cur = mysql.connection.cursor()
    if search_query:
        cur.execute("SELECT * FROM products WHERE name LIKE %s LIMIT %s OFFSET %s", (f"%{search_query}%", per_page, offset))
    else:
        cur.execute("SELECT * FROM products LIMIT %s OFFSET %s", (per_page, offset))
    products = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM products WHERE name LIKE %s", (f"%{search_query}%",))
    total = cur.fetchone()[0]
    cur.close()
    
    
    
    return render_template('index.html', products=products, search_query=search_query, page=page, total=total, per_page=per_page)

# Add Product
@app.route('/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        
        # Generated random primray key
        key = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products (p_id,name, price, quantity) VALUES (%s,%s, %s, %s)", (key,name, price, quantity))
        mysql.connection.commit()
        cur.close()
        flash("Product Added Successfully!", "success")
        return redirect(url_for('index'))

# Edit Product
@app.route('/edit/<string:id>', methods=['GET', 'POST']) # <int:id>
def edit_product(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products WHERE p_id = %s", (id,))
    product = cur.fetchone()
    cur.close()
    
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE products SET name = %s, price = %s, quantity = %s WHERE p_id = %s", (name, price, quantity, id))
        mysql.connection.commit()
        cur.close()
        flash("Product Updated Successfully!", "success")
        return redirect(url_for('index'))
    
    return render_template('edit.html', product=product)

# Delete Product
@app.route('/delete/<string:id>')
def delete_product(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM products WHERE p_id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    flash("Product Deleted Successfully!", "danger")
    return redirect(url_for('index'))

# Stack Operations
@app.route('/stack/push', methods=['POST'])
def push_stack():
    value = request.form['value']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO stack_table (value) VALUES (%s)", (value,))
    mysql.connection.commit()
    cur.close()
    flash("Value Pushed to Stack!", "success")
    return redirect(url_for('index'))

@app.route('/stack/pop')
def pop_stack():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, value FROM stack_table ORDER BY s_id DESC LIMIT 1")
    row = cur.fetchone()
    if row:
        cur.execute("DELETE FROM stack_table WHERE s_id = %s", (row[0],))
        mysql.connection.commit()
        flash(f"Popped: {row[1]}", "danger")
    else:
        flash("Stack is Empty!", "warning")
    cur.close()
    return redirect(url_for('index'))

# Queue Operations
@app.route('/queue/enqueue', methods=['POST'])
def enqueue_queue():
    value = request.form['value']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO queue_table (value) VALUES (%s)", (value,))
    mysql.connection.commit()
    cur.close()
    flash("Value Enqueued!", "success")
    return redirect(url_for('index'))

@app.route('/queue/dequeue')
def dequeue_queue():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, value FROM queue_table ORDER BY id ASC LIMIT 1")
    row = cur.fetchone()
    if row:
        cur.execute("DELETE FROM queue_table WHERE id = %s", (row[0],))
        mysql.connection.commit()
        flash(f"Dequeued: {row[1]}", "danger")
    else:
        flash("Queue is Empty!", "warning")
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    logging.info("Running the main function.")
    app.run(debug=True,port='5000',host='0.0.0.0')
