import os
import pytest
from datetime import datetime
from utils.driver_factory import inicializar_driver
from utils.helpers import cargar_datos_prueba
from utils.logger import obtener_logger

logger = obtener_logger()

@pytest.fixture(scope="session")
def test_data():
    return cargar_datos_prueba()

@pytest.fixture(scope="function")
def driver(request):
    # Permite pasar headless por linea de comandos si se define
    headless = request.config.getoption("--headless", default=False)
    driver_instance = inicializar_driver(headless=headless)
    logger.info(f"Iniciando navegador para caso de prueba: {request.node.name}")
    yield driver_instance
    logger.info(f"Cerrando navegador para caso de prueba: {request.node.name}")
    driver_instance.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Ejecutar pruebas en modo headless (sin interfaz grafica)"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        if report.failed:
            driver = item.funcargs.get("driver")
            if driver:
                carpeta_capturas = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "screenshots")
                os.makedirs(carpeta_capturas, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                nombre_archivo = f"{item.name}_{timestamp}.png"
                ruta_captura = os.path.join(carpeta_capturas, nombre_archivo)
                driver.save_screenshot(ruta_captura)
                logger.error(f"Test fallido: {item.name}. Captura guardada en: {ruta_captura}")

                # Adjunta la captura al reporte HTML si pytest-html esta disponible
                try:
                    import pytest_html
                    extras.append(pytest_html.extras.image(ruta_captura))
                except Exception:
                    pass
        report.extras = extras

def pytest_html_report_title(report):
    report.title = "Reporte de Automatizacion Saucedemo - Florencia Adamo"

