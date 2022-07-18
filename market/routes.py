from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')  # Decorator, website navigation
@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html')    # Importing template from templates folder

@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        purchase_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchase_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f'Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$', category='success')
            else:
                flash(f'Sorry! Not enough cash to purchase {p_item_object.name}', category='danger')

        return redirect(url_for('market_page'))

    if request.method == 'GET':
        items = Item.query.filter_by(owner=None)    # Get all elements from table Item without owner
        return render_template('market.html', items=items, purchase_form=purchase_form) #Send data to html

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'User created successfully! You are now logged in as {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:   # If there are no errors from validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Logged in successfully as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f'Username and password are incorrect. Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f'User successfully logged out', category='info')
    return redirect(url_for('home_page'))
