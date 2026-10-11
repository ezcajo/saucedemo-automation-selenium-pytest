import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "/inventory.html" in driver.current_url, "error: No se dirigió a la página de inventario después del inicio de sesión"

def test_verificar_pagina_inventario(driver):
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text
    assert section_title == "Products", "error: El título de la sección de inventario no es 'Products'"
    assert page_title == "Swag Labs", "error: El título de la página de inventario no coincide con el esperado"

def test_productos_visibles(driver):
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "error: No se encontraron productos visibles en la página de inventario"

def tes_validar_interfaz_usuario(driver):
    # Verificar que el menú de usuario esté presente
    menu_usuario = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro_usuario = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu_usuario.is_displayed(), "error: El menú de usuario no está visible en la página de inventario"
    assert filtro_usuario.is_displayed(), "error: El filtro de usuario no está visible en la página de inventario"

def test_agregar_producto_al_carrito(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1", "error: El producto no se agregó correctamente al carrito"

def test_verificar_carrito(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "/cart.html" in driver.current_url, "error: No se dirigió a la página del carrito después de hacer clic en el carrito"
    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(productos_carrito) == 1, "error: El carrito no contiene el producto agregado"

def test_navegar_carrito(driver):
   driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
   assert "/cart.html" in driver.current_url, "error: No se dirigió a la página del carrito después de hacer clic en el ícono del carrito"

def test_comprobar_producto_en_carrito(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == "Sauce Labs Backpack", "error: El producto en el carrito no coincide con el producto agregado"   