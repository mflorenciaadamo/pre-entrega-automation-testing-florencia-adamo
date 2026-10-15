import logging
import os

def obtener_logger(nombre="QA_Logger"):
    logger = logging.getLogger(nombre)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formato = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

        consola = logging.StreamHandler()
        consola.setFormatter(formato)
        logger.addHandler(consola)

        carpeta_reports = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
        os.makedirs(carpeta_reports, exist_ok=True)
        archivo_log = os.path.join(carpeta_reports, "ejecucion.log")
        manejador_archivo = logging.FileHandler(archivo_log, encoding="utf-8")
        manejador_archivo.setFormatter(formato)
        logger.addHandler(manejador_archivo)

    return logger

