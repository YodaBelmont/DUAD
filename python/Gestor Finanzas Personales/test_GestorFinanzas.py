import os
from datetime import datetime, timedelta

import pytest

import LogicManagement



@pytest.fixture
def manager():
    for file in ("Categories_list.csv", "Transactions_data.csv"):
        if os.path.exists(file):
            os.remove(file)

    return LogicManagement.Finance_Manager()


def test_has_categories_returns_false(manager):
    assert manager.has_categories() is False


def test_get_category_adds_category(manager):
    manager.get_category("Food", "red")

    assert len(manager.categories) == 1
    assert manager.categories[0].category == "Food"
    assert manager.categories[0].color == "red"


def test_has_categories_returns_true(manager):
    manager.get_category("Food", "red")

    assert manager.has_categories() is True


def test_category_names_returns_all_names(manager):
    manager.get_category("Food", "red")
    manager.get_category("Bills", "blue")
    manager.get_category("Games", "green")

    assert manager.category_names == ["Food", "Bills", "Games"]


@pytest.mark.parametrize("value", [
    "10",
    "10.5",
    "0",
    "-25.3"
])
def test_to_float_accepts_numbers(manager, value):
    assert manager.to_float(value)


@pytest.mark.parametrize("value", [
    "",
    "abc",
    "10abc",
    "hola"
])
def test_to_float_rejects_invalid_values(manager, value):
    assert not manager.to_float(value)


def test_check_values_returns_true(manager):
    values = {
        "title": "Salary",
        "amount": "1000",
        "category_list": "Work",
        "date": "01/01/2025"
    }

    assert manager.check_values(values)


def test_check_values_returns_false(manager):
    values = {
        "title": "",
        "amount": "1000",
        "category_list": "Work",
        "date": "01/01/2025"
    }

    assert not manager.check_values(values)


def test_validate_date_accepts_today(manager):
    today = datetime.today().strftime("%d/%m/%Y")

    assert manager.validate_date(today)


def test_validate_date_rejects_future_date(manager):
    future = (datetime.today() + timedelta(days=1)).strftime("%d/%m/%Y")

    assert not manager.validate_date(future)


def test_create_transaction(manager):
    manager.get_category("Food", "red")

    values = {
        "title": "Pizza",
        "amount": "15",
        "category_list": "Food",
        "date": "01/01/2025"
    }

    manager.create_transaction("OUTCOME", values)

    assert len(manager.transactions) == 1

    transaction = manager.transactions[0]

    assert transaction.title == "Pizza"
    assert transaction.amount == 15.0
    assert transaction.transaction_type == "OUTCOME"
    assert transaction.category.category == "Food"


def test_table_rows_returns_correct_data(manager):
    manager.get_category("Food", "red")

    values = {
        "title": "Pizza",
        "amount": "15",
        "category_list": "Food",
        "date": "01/01/2025"
    }

    manager.create_transaction("OUTCOME", values)

    assert manager.table_rows == [
        ["Pizza", 15.0, "OUTCOME", "Food", "01/01/2025"]
    ]


def test_filter_table_returns_only_transactions_in_range(manager):
    manager.get_category("Food", "red")

    manager.create_transaction("OUTCOME", {
        "title": "Pizza",
        "amount": "20",
        "category_list": "Food",
        "date": "01/01/2025"
    })

    manager.create_transaction("OUTCOME", {
        "title": "Burger",
        "amount": "15",
        "category_list": "Food",
        "date": "15/01/2025"
    })

    manager.create_transaction("OUTCOME", {
        "title": "Soda",
        "amount": "5",
        "category_list": "Food",
        "date": "01/03/2025"
    })

    filtered = manager.filter_table("01/01/2025", "31/01/2025")

    assert len(filtered) == 2
    assert filtered[0].title == "Pizza"
    assert filtered[1].title == "Burger"


def test_color_rows_returns_correct_colors(manager):
    manager.get_category("Food", "red")
    manager.get_category("Games", "blue")

    manager.create_transaction("OUTCOME", {
        "title": "Pizza",
        "amount": "20",
        "category_list": "Food",
        "date": "01/01/2025"
    })

    manager.create_transaction("OUTCOME", {
        "title": "Steam",
        "amount": "30",
        "category_list": "Games",
        "date": "02/01/2025"
    })

    assert manager.color_rows(manager.transactions) == [
        (0, "white", "red"),
        (1, "white", "blue")
    ]


def test_save_and_check_data(manager):
    manager.get_category("Food", "red")

    manager.create_transaction("OUTCOME", {
        "title": "Pizza",
        "amount": "20",
        "category_list": "Food",
        "date": "01/01/2025"
    })

    manager.save_data()

    new_manager = LogicManagement.Finance_Manager()
    new_manager.check_data()

    assert len(new_manager.categories) == 1
    assert len(new_manager.transactions) == 1

    assert new_manager.categories[0].category == "Food"
    assert new_manager.transactions[0].title == "Pizza"