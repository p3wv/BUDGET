from flask import render_template, Blueprint

from budget_app.models import Transaction

main = Blueprint('main', __name__)

# Strona główna
@main.route('/')
def index():
    transactions = Transaction.query.all()
    return render_template('index.html', transactions=transactions)