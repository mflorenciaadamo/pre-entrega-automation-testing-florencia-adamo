from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Localizadores como tuplas
        self.title = (By.CLASS_NAME, "title")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.sort_container = (By.CLASS_NAME, "product_sort_container")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")

    def obtener_titulo(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self.title))
        return elemento.text.strip()

    def verificar_elementos_interfaz(self):
        menu = self.wait.until(EC.visibility_of_element_located(self.menu_button))
        filtro = self.wait.until(EC.visibility_of_element_located(self.sort_container))
        carrito = self.wait.until(EC.visibility_of_element_located(self.cart_link))
        return menu.is_displayed() and filtro.is_displayed() and carrito.is_displayed()

    def obtener_productos(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.inventory_items))

    def obtener_datos_primer_producto(self):
        productos = self.obtener_productos()
        primer_item = productos[0]
        nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
        precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip()
        return nombre, precio

    def agregar_primer_producto_al_carrito(self):
        productos = self.obtener_productos()
        primer_item = productos[0]
        nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
        precio = primer_item.find_element(By.CLASS_NAME, "inventory_item_price").text.strip()
        boton_agregar = primer_item.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        boton_agregar.click()
        return nombre, precio

    def obtener_cantidad_carrito(self):
        badge = self.wait.until(EC.visibility_of_element_located(self.cart_badge))
        return badge.text.strip()

    def ir_al_carrito(self):
        link = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        link.click()

