import pytest
import os
from budget tracking import *

def test_valid_expense():
    expense = Expense(1, 500, "Warzywa")
    assert expense.id == 1
    assert expense.amount == 500
    assert expense.description == "Warzywa"

def test_invalid_expense():
    with pytest.raises(ValueError):
        Expense(2, 0, "Invalid Expense")

def test_is_big():
    expense1 = Expense(3,1500, "Big Expense")
    expense2 = Expense(4, 500, "Small Expense")
    assert expense1.is_big() is True
    assert expense2.is_big() is False


def test_find_new_id():
    expenses = [Expense(1, 100, "Expense 1"), Expense(3, 200, "Expense 2")]
    next_id = find_new_id(expenses)
    assert next_id == 2

def test_empty_expenses():
    expenses = []
    next_id = find_new_id(expenses)
    assert next_id == 1

def test_compute_total():
    expenses = [Expense(1, 100, "Expense 1"), Expense(2, 200, "Expense 2")]
    total = compute_total(expenses)
    assert total == 300
