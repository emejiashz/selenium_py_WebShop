# Web Shop Test Suite

Este es un proyecto de prueba automatizado para un marketplace (ejemplo basado en Amazon) utilizando el Page Object Model (POM), pytest y Selenium.

## Estructura del Proyecto


│
├── config/
│ └── config.json
├── tests/
│ ├── conftest.py
│ ├── test_base.py
│ ├── test_login.py
│ ├── test_search.py
│ ├── test_purchase.py
│ └── test_account.py
└── pages/
├── base_page.py
├── login_page.py
├── search_results_page.py
├── product_page.py
├── cart_page.py
├── account_page.py
└── home_page.py