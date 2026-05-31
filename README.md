# Cash Register OOP Lab

This repository contains a `CashRegister` class modeled for an e-commerce checkout flow.

## Features

- `discount` attribute with validation for values between 0 and 100
- `total` amount tracking
- `items` list storing added item names
- `previous_transactions` list storing item/price/quantity dictionaries
- `add_item(item, price, quantity)` method
- `apply_discount()` method applying percentage discount to total
- `void_last_transaction()` method removing the most recent transaction

## Run tests

```bash
pip install pytest
pytest -q
```
