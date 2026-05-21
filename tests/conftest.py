import pytest


@pytest.fixture
def valid_form_request():
    return {
        "name": "Tupu",
        "last_name": "Tamadre",
        "dni": "12345678",
        "phone": "1144556677",
        "email": "tupu@tamadre.com",
        "dniImage": "https://example.com/dni.jpg",
        "taxImage": "https://example.com/tax.jpg",
        "form_type": "Register",
    }

@pytest.fixture
def valid_form_request2():
    return {
        "name": "Tupu",
        "last_name": "Tamadre",
        "dni": "12345678",
        "phone": "1144556677",
        "email": "tupu@tamadre2.com",
        "dniImage": "https://example.com/dni.jpg",
        "taxImage": "https://example.com/tax.jpg",
        "form_type": "Register",
    }

@pytest.fixture
def invalid_form_request():
    return {
        "name": "Tupu",
        "last_name": "Tamadre",
        "dni": "12345678",
        "phone": "1144556677",
        "email": "tupu@tamadre.com",
        "dniImage": "https://example.com/dni.jpg",
        "taxImage": "https://example.com/tax.jpg",
        "form_type": "2131232",
    }


