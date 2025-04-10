# Importa la clase By para localizar elementos HTML con distintas estrategias (XPATH, ID, NAME, etc.)
from selenium.webdriver.common.by import By

# Importa la clase base que contiene funciones reutilizables como click, wait, send_keys, etc.
from pages.base_page import BasePage

class DevicesPage(BasePage):
    """
    Representa la página de 'Dispositivos' dentro del flujo de pruebas automatizadas.
    Hereda métodos reutilizables desde BasePage para realizar acciones comunes.
    """

    # Localizador del botón "Siguiente" usando una ruta absoluta XPath
    NEXT_BTN = (By.XPATH, '/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/div[2]/div/button')

    def proceed(self):
        """
        Realiza la acción de avanzar en la página haciendo clic en el botón 'Siguiente'.
        Se agrega una espera fija de 5 segundos antes de hacer clic, útil en entornos donde 
        el botón puede demorar en activarse o renderizarse completamente.
        """
        self.wait_seconds(5)        # Espera explícita de 5 segundos
        self.click(self.NEXT_BTN)   # Hace clic en el botón Siguiente
