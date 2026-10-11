# Automatización de pruebas de SauceDemo

Este proyecto automatiza pruebas funcionales sobre [SauceDemo](https://www.saucedemo.com/) mediante Selenium y Pytest. La suite verifica el inicio de sesión, la visualización del inventario, la incorporación de un producto al carrito y la navegación del carrito.

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- pytest-html, para generar reportes HTML
- webdriver-manager, para descargar y configurar ChromeDriver automáticamente

## Instalación

1. Cloná el repositorio y accedé al directorio del proyecto.
2. Creá y activá un entorno virtual (recomendado):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instalá las dependencias:

   ```powershell
   pip install -r requirements.txt
   ```

Para ejecutar las pruebas es necesario tener Google Chrome instalado y conexión a internet la primera vez, para que `webdriver-manager` obtenga el controlador compatible.

## Ejecución de pruebas

Ejecutá la suite completa con salida detallada:

```powershell
pytest tests/test_saucedemo.py -v
```

## Reporte HTML

Generá el reporte de la ejecución con:

```powershell
pytest tests/test_saucedemo.py -v --html=reporte.html --self-contained-html
```

El archivo `reporte.html` se creará en la raíz del proyecto y puede abrirse en cualquier navegador.
