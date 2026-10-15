import pytest
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from utils.logger import obtener_logger

logger = obtener_logger()

def test_01_login_exitoso(driver, test_data):
    logger.info("Iniciando prueba: Login exitoso con Page Object Model")
    driver.get(test_data["base_url"])

    login_page = LoginPage(driver)
    login_page.hacer_login(
        test_data["users"]["standard"]["username"],
        test_data["users"]["standard"]["password"]
    )

    inventory_page = InventoryPage(driver)
    titulo_pagina = inventory_page.obtener_titulo()
    logo_app = login_page.obtener_logo()

    assert test_data["endpoints"]["inventory"] in driver.current_url, (
        f"URL incorrecta tras login: {driver.current_url}"
    )
    assert titulo_pagina == test_data["expected_texts"]["inventory_title"]
    assert logo_app == test_data["expected_texts"]["app_title"]
    logger.info("Login exitoso validado correctamente.")

def test_02_navegacion_catalogo(driver, test_data):
    logger.info("Iniciando prueba: Navegacion y catalogo de productos")
    driver.get(test_data["base_url"])

    login_page = LoginPage(driver)
    login_page.hacer_login(
        test_data["users"]["standard"]["username"],
        test_data["users"]["standard"]["password"]
    )

    inventory_page = InventoryPage(driver)
    titulo_seccion = inventory_page.obtener_titulo()
    assert titulo_seccion == test_data["expected_texts"]["inventory_title"]

    assert inventory_page.verificar_elementos_interfaz(), (
        "No todos los elementos de la interfaz estan visibles (menu, filtro o carrito)"
    )

    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "No se encontraron productos en el catalogo"

    nombre_prod, precio_prod = inventory_page.obtener_datos_primer_producto()
    assert len(nombre_prod) > 0, "El nombre del primer producto esta vacio"
    assert precio_prod.startswith("$"), f"Formato de precio invalido: {precio_prod}"

    logger.info(f"Primer producto detectado -> Nombre: {nombre_prod} | Precio: {precio_prod}")

def test_03_interaccion_carrito(driver, test_data):
    logger.info("Iniciando prueba: Agregar producto al carrito")
    driver.get(test_data["base_url"])

    login_page = LoginPage(driver)
    login_page.hacer_login(
        test_data["users"]["standard"]["username"],
        test_data["users"]["standard"]["password"]
    )

    inventory_page = InventoryPage(driver)
    nombre_esperado, precio_esperado = inventory_page.agregar_primer_producto_al_carrito()

    cantidad_carrito = inventory_page.obtener_cantidad_carrito()
    assert cantidad_carrito == "1", f"Contador del carrito inesperado: {cantidad_carrito}"

    inventory_page.ir_al_carrito()
    assert test_data["endpoints"]["cart"] in driver.current_url

    cart_page = CartPage(driver)
    items_carrito = cart_page.obtener_items()
    assert len(items_carrito) == 1, f"Se esperaba 1 item en carrito, hay {len(items_carrito)}"

    nombre_obtenido, precio_obtenido = cart_page.obtener_datos_primer_item()
    assert nombre_obtenido == nombre_esperado
    assert precio_obtenido == precio_esperado

    logger.info(f"Producto '{nombre_esperado}' verificado con exito en el carrito.")
