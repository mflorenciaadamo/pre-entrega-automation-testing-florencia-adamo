from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def inicializar_driver(headless=False):
    opciones = Options()
    if headless:
        opciones.add_argument("--headless=new")
    opciones.add_argument("--start-maximized")
    opciones.add_argument("--incognito")
    opciones.add_argument("--lang=es")
    opciones.add_argument("--disable-notifications")
    opciones.add_argument("--disable-search-engine-choice-screen")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=opciones)
    driver.implicitly_wait(10)
    return driver

