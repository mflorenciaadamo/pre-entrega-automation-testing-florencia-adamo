import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def cargar_datos_prueba():
    ruta = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datos", "test_data.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def esperar_elemento_visible(driver, by, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, locator)))

def esperar_elementos_visibles(driver, by, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_all_elements_located((by, locator)))

def esperar_elemento_clickeable(driver, by, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, locator)))

def escribir_texto(driver, by, locator, texto, timeout=10):
    elemento = esperar_elemento_visible(driver, by, locator, timeout)
    elemento.clear()
    elemento.send_keys(texto)
    return elemento

def hacer_click(driver, by, locator, timeout=10):
    elemento = esperar_elemento_clickeable(driver, by, locator, timeout)
    elemento.click()
    return elemento

def obtener_texto(driver, by, locator, timeout=10):
    elemento = esperar_elemento_visible(driver, by, locator, timeout)
    return elemento.text.strip()

def iniciar_sesion(driver, usuario=None, password=None):
    datos = cargar_datos_prueba()
    usr = usuario or datos["users"]["standard"]["username"]
    pwd = password or datos["users"]["standard"]["password"]

    driver.get(datos["base_url"])
    escribir_texto(driver, By.ID, "user-name", usr)
    escribir_texto(driver, By.ID, "password", pwd)
    hacer_click(driver, By.ID, "login-button")
    esperar_elemento_visible(driver, By.CLASS_NAME, "title")

