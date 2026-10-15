from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Localizadores como tuplas
        self.title = (By.CLASS_NAME, "title")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")

    def obtener_items(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.cart_items))

    def obtener_datos_primer_item(self):
        items = self.obtener_items()
        primer_item = items[0]
        nombre = primer_item.find_element(*self.item_name).text.strip()
        precio = primer_item.find_element(*self.item_price).text.strip()
        return nombre, precio

