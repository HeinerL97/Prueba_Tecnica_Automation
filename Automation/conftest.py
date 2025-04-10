#Importacion de la librerias a utilization
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def driver():
    """
    Fixture de Pytest que configura e inicializa el navegador Chrome usando Selenium WebDriver.

    Este fixture se encarga de:
    1. Construir la ruta absoluta al ejecutable de ChromeDriver.
    2. Establecer opciones del navegador (como iniciar maximizado).
    3. Crear una instancia del navegador Chrome con las configuraciones definidas.
    4. Establecer un tiempo de espera implícito de 10 segundos.
    5. Entregar el `driver` para que sea usado en las pruebas.
    6. Cerrar el navegador una vez finaliza la prueba.

    Retorna:
        driver (webdriver.Chrome): Instancia activa del navegador Chrome.
    """

    # Ruta al ejecutable del ChromeDriver dentro del proyecto
    chromedriver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")

    # Opciones del navegador: abrir maximizado
    options = Options()
    options.add_argument("--start-maximized")

    # Servicio de ChromeDriver
    service = Service(executable_path=chromedriver_path)

    # Inicialización del navegador
    driver = webdriver.Chrome(service=service, options=options)

    # Espera implícita para búsqueda de elementos
    driver.implicitly_wait(10)

    # Devuelve el navegador para ser usado en la prueba
    yield driver

    # Cierra el navegador después de la prueba
    driver.quit()
