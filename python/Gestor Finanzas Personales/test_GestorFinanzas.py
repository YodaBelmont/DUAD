import pytest
import Data as data
import Entities as entity


def test_create_category():
    category = entity.Category("Food")

    assert category.category == "Food"


def test_create_transaction():
    transaction = entity.Transaction(
        "Pizza",
        "5000",
        "Outcome",
        "Food",
        "15/06/2026"
    )

    assert transaction.title == "Pizza"
    assert transaction.amount == "5000"
    assert transaction.transaction_type == "Outcome"
    assert transaction.category == "Food"
    assert transaction.date == "15/06/2026"


def test_get_category_adds_category():
    categories = []

    entity.get_category(categories, "Food")

    assert categories == ["Food"]


def test_get_transaction_adds_transaction():
    entities_table = []
    table_rows = []

    values = {
        "title": "Pizza",
        "amount": "5000",
        "types": "Outcome",
        "category_list": "Food",
        "date": "15/06/2026"
    }

    entity.get_transaction(
        entities_table,
        table_rows,
        values
    )

    assert len(entities_table) == 1


def test_transaction_to_row():
    transaction = entity.Transaction(
        "Salary",
        "1000",
        "Income",
        "Work",
        "01/01/2026"
    )

    assert transaction.to_row() == [
        "Salary",
        "1000",
        "Income",
        "Work",
        "01/01/2026"
    ]


def test_get_category_multiple():
    categories = []

    entity.get_category(categories, "Food")
    entity.get_category(categories, "Transport")

    assert len(categories) == 2


def test_write_and_import_csv():
    rows = [
        ["Pizza", "5000", "Outcome", "Food", "15/06/2026"],
        ["Salary", "1000", "Income", "Work", "01/06/2026"]
    ]

    data.write_csv(rows)

    imported_rows = data.import_csv()

    assert imported_rows == rows


def test_get_transaction_creates_row():
    entities_table = []
    table_rows = []

    values = {
        "title": "Pizza",
        "amount": "5000",
        "types": "Outcome",
        "category_list": "Food",
        "date": "15/06/2026"
    }

    entity.get_transaction(
        entities_table,
        table_rows,
        values
    )

    assert table_rows == [
        ["Pizza", "5000", "Outcome", "Food", "15/06/2026"]
    ]