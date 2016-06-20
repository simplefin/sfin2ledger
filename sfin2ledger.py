import sys
import json
import argparse
from decimal import Decimal
from datetime import datetime


def simplefin2Ledger(intext):
    data = json.loads(intext)
    err = ''
    all_trans = []
    for account in data['accounts']:
        for transaction in account['transactions']:
            transaction['account'] = account
            all_trans.append(transaction)
    all_trans = sorted(all_trans, key=lambda x:x['posted'])
    lines = []
    for trans in all_trans:
        posted = datetime.fromtimestamp(trans['posted']).strftime('%Y/%m/%d')
        lines.append('{0} {1}'.format(posted, trans['description']))
        amount = Decimal(trans['amount'])
        approx_width = 40

        if amount > 0:
            # income
            name = 'Assets:{0}'.format(trans['account']['name'])
            amount = '${0}'.format(abs(amount))
            space = ' '*(approx_width-len(name)-len(amount))
            lines.append('    {name}{space}{amount}'.format(
                name=name,
                space=space,
                amount=amount))
            lines.append('    Income:UNKNOWN')
        else:
            # expense
            name = 'Expenses:UNKNOWN'
            amount = '${0}'.format(abs(amount))
            space = ' '*(approx_width-len(name)-len(amount))
            lines.append('    {name}{space}{amount}'.format(
                name=name,
                space=space,
                amount=amount))
            lines.append('    Assets:{0}'.format(trans['account']['name']))
        lines.append('')
        lines.append('')
    return '\n'.join(lines), err


ap = argparse.ArgumentParser('ledger-pull')

def run(args=None):
    args = ap.parse_args(args)
    stdin = sys.stdin.read()
    out, err = simplefin2Ledger(stdin)
    sys.stdout.write(out)
    sys.stderr.write(err)
