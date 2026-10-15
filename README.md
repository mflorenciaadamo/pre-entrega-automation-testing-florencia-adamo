# Pre-Entrega Automation Testing - Florencia Adamo
--

## Descripcion
Proyecto de automatización de pruebas realizado con Python, Selenium WebDriver y Pytest

El objetivo del proyecto es automatizar distintas pruebas funcionales de una aplicación web.

---

##  Tecnologias en uso

-  Python 3.10+
- Framework  Pytest
- Herramienta de Automatizacion Web: Selenium WebDriver
-Generador de Reportes pytest-html 
- Control de Versiones: Git y GitHub

---

##  Casos de Prueba 

| ID | Test |

| 01  `test_01_login_exitoso` 
| 02  `test_02_navegacion_catalogo` 
| 03  `test_03_interaccion_carrito` 

---



## Instalacion 
### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/mflorenciaadamo/pre-entrega-automation-testing-florencia-adamo.git
cd pre-entrega-automation-testing-florencia-adamo
```

### Paso 2: Crear y activar entorno virtual (Recomendado)
- En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

---

### Ejecucion de Pruebas y Reporte

Gracias a la configuracion en `pytest.ini`, para correr todas las pruebas y generar automaticamente el reporte HTML con CSS externo solo necesitas ejecutar:

```bash
python -m pytest
```



### Opciones de ejecucion adicionales:
- **Modo Headless (sin abrir la ventana del navegador):**
  ```bash
  python -m pytest --headless
  ```
- **Ejecutar unicamente el archivo de pruebas:**
  ```bash
  python -m pytest tests/test_saucedemo.py
  ```

---

## Reportes y Evidencias

- **Reporte HTML:** Se genera de forma automatica en `reports/reporte.html`.
- **CSS Desacoplado:** Ubicado en `reports/assets/style.css`, aplicando estilos externos limpios.
- **Logs de Ejecucion:** Se registran en `reports/ejecucion.log` y en consola en tiempo real.
- **Capturas de Pantalla:** Si una prueba falla, se guarda una captura `.png` en `reports/screenshots/` y se adjunta de manera automatica en el reporte HTML.
