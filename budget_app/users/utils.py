import csv
import io
from flask import app, Response, Blueprint
from models import Transaction

export = Blueprint('export', __name__)

# Eksport danych
@export.route('/export_transactions')
def export_transactions():
    transactions = Transaction.query.all()
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'Title', 'Amount', 'Type'])
    for transaction in transactions:
        cw.writerow([transaction.id, transaction.title,
                    transaction.amount, transaction.type.value])

    output = si.getvalue()
    return Response(output, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=transactions.csv"})