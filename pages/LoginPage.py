from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Localizadores como tuplas (patron POM)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.app_logo = (By.CLASS_NAME, "app_logo")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def ingresar_usuario(self, usuario):
        elemento = self.wait.until(EC.visibility_of_element_located(self.username_input))
        elemento.clear()
        elemento.send_keys(usuario)

    def ingresar_password(self, password):
        elemento = self.wait.until(EC.visibility_of_element_located(self.password_input))
        elemento.clear()
        elemento.send_keys(password)

    def click_login(self):
        elemento = self.wait.until(EC.element_to_be_clickable(self.login_button))
        elemento.click()

    def hacer_login(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.click_login()

    def obtener_logo(self):
        elemento = self.wait.until(EC.visibility_of_element_located(self.app_logo))
        return elemento.text.strip()

