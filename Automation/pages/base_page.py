# Importación de clases necesarias de Selenium para manejo de condiciones de espera y selección de elementos en listas desplegables
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Clase base para representar una página en un framework de automatización web con Selenium.
    Contiene métodos reutilizables para interactuar con elementos de la interfaz.
    """

    def __init__(self, driver):
        """
        Constructor de la clase BasePage.

        driver: instancia del WebDriver (por ejemplo, Chrome, Firefox) para controlar el navegador.
        """
        self.driver = driver

    def click(self, by_locator):
        """
        Hace clic en un elemento una vez que sea clickeable.

       by_locator: tupla (estrategia, valor), por ejemplo (By.ID, "boton_login")
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, text):
        """
        Envía texto a un campo de entrada una vez que sea visible.

        by_locator: tupla con la ubicación del elemento.
         text: texto que se desea escribir en el campo.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        """
        Obtiene el texto visible de un elemento.

         by_locator: tupla con la ubicación del elemento.
        :return: texto contenido en el elemento.
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def select_option(self, by_locator):
        """
        Hace clic sobre una opción de selección .

         by_locator: tupla con la ubicación del elemento.
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def wait_seconds(self, seconds):
        """
        Espera de forma explícita por una cantidad de segundos.

         seconds: número de segundos a esperar (no recomendado para pruebas dinámicas).
        """
        import time
        time.sleep(seconds)

    def wait_for_element(self, by_locator, timeout=10):
        """
        Espera hasta que un elemento esté presente (no necesariamente visible).

        by_locator: tupla con la ubicación del elemento.
         timeout: tiempo máximo de espera (por defecto 10 segundos).
        return: el elemento ubicado.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))

    def select_dropdown_by_text(self, locator, visible_text):
        """
        Selecciona una opción de un menú desplegable usando el texto visible.

        locator: tupla con la ubicación del <select>.
        visible_text: texto visible de la opción a seleccionar.
        """
        element = self.wait_for_element(locator)
        select = Select(element)
        select.select_by_visible_text(visible_text)
