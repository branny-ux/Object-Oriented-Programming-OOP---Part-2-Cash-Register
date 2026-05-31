import pytest
from lib.cash_register import CashRegister


def test_register_initializes_with_default_discount():
    reg = CashRegister()
    assert reg.discount == 0
    assert reg.total == 0
    assert reg.items == []
    assert reg.previous_transactions == []


def test_register_initializes_with_discount():
    reg = CashRegister(20)
    assert reg.discount == 20


def test_invalid_discount_prints_error_and_sets_zero(capfd):
    reg = CashRegister(150)
    captured = capfd.readouterr()
    assert "Not valid discount" in captured.out
    assert reg.discount == 0


def test_add_item_updates_total_items_and_transactions():
    reg = CashRegister()
    reg.add_item("Book", 15, 2)
    assert reg.total == 30
    assert reg.items == ["Book", "Book"]
    assert reg.previous_transactions == [{"item": "Book", "price": 15, "quantity": 2}]


def test_apply_discount_reduces_total(capfd):
    reg = CashRegister(10)
    reg.add_item("Notebook", 20, 1)
    reg.apply_discount()
    assert reg.total == 18


def test_apply_discount_with_no_transactions_prints_message(capfd):
    reg = CashRegister(25)
    reg.apply_discount()
    captured = capfd.readouterr()
    assert "There is no discount to apply." in captured.out


def test_void_last_transaction_removes_last_item():
    reg = CashRegister()
    reg.add_item("Pen", 3, 3)
    reg.add_item("Pencil", 2, 1)
    reg.void_last_transaction()
    assert reg.total == 9
    assert reg.items == ["Pen", "Pen", "Pen"]
    assert reg.previous_transactions == [{"item": "Pen", "price": 3, "quantity": 3}]
