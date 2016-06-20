# SimpleFIN 2 Ledger

sfin2ledger is a command line utility to convert [SimpleFIN account data](https://www.simplefin.org/protocol.html) to a format suitable for [Ledger](http://ledger-cli.org/index.html).

## Installation

```bash
pip install git+https://github.com/simplefin/sfin2ledger.git
```

## Example

Find your bank's SimpleFIN server.  If they don't have one, you can use the [SimpleFIN Bridge](https://bridge.simplefin.org/simple/).  The example below uses a demo account from the SimpleFIN Bridge.

Claim an access url (you do this once you have a Setup Token):

```bash
SETUP_TOKEN="aHR0cHM6Ly9icmlkZ2Uuc2ltcGxlZmluLm9yZy9zaW1wbGVmaW4vY2xhaW0vZGVtbw=="
CLAIM_URL=$(echo ${SETUP_TOKEN} | base64 --decode)
ACCESS_URL=$(curl -X POST $CLAIM_URL)
echo "$ACCESS_URL" > /tmp/access_url
```

Get some data in ledger format (do this daily or whatever):

```bash
curl "$(cat /tmp/access_url)/accounts" | sfin2ledger
```
