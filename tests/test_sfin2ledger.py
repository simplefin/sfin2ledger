# import pytest
import json
from sfin2ledger import simplefin2Ledger


def test_basic():
    sample = json.dumps({
      "errors": [],
      "accounts": [
        {
          "org": {
            "domain": "mybank.com",
            "sfin-url": "https://sfin.mybank.com"
          },
          "id": "2930002",
          "name": "Savings",
          "currency": "USD",
          "balance": "100.23",
          "available-balance": "75.23",
          "balance-date": 978366153,
          "transactions": [
            {
              "id": "12394832938403",
              "posted": 793090572,
              "amount": "-33293.43",
              "description": "Uncle Frank's Bait Shop",
            }
          ],
          "extra": {
            "account-open-date": 978360153,
          }
        }
      ]
    })
    out, err = simplefin2Ledger(sample)
    assert out == (
        "1995/02/17 Uncle Frank's Bait Shop\n"
        "    Expenses:UNKNOWN               $33293.43\n"
        "    Assets:Savings\n\n")
    assert err == ''

def test_credit():
    sample = json.dumps({
      "errors": [],
      "accounts": [
        {
          "org": {
            "domain": "mybank.com",
            "sfin-url": "https://sfin.mybank.com"
          },
          "id": "2930002",
          "name": "Savings",
          "currency": "USD",
          "balance": "100.23",
          "available-balance": "75.23",
          "balance-date": 978366153,
          "transactions": [
            {
              "id": "12394832938403",
              "posted": 793090572,
              "amount": "2250.22",
              "description": "Payroll Payment",
            }
          ],
          "extra": {
            "account-open-date": 978360153,
          }
        }
      ]
    })
    out, err = simplefin2Ledger(sample)
    assert out == (
        "1995/02/17 Payroll Payment\n"
        "    Assets:Savings                  $2250.22\n"
        "    Income:UNKNOWN\n\n")
    assert err == ''