# Importa time para pausas si son necesarias (aunque no se usa directamente en esta clase)
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    Representa la página de inicio (Home) del sitio web.
    Hereda de BasePage para acceder a métodos reutilizables en pruebas automatizadas.
    """

    # Localizador del botón para aceptar cookies (generalmente mostrado al entrar al sitio)
    COOKIE_BTN = (By.ID, "onetrust-accept-btn-handler")

    def accept_cookies(self):
        """
        Hace clic en el botón de aceptación de cookies.
        Se utiliza para cerrar el banner de cookies al cargar la página por primera vez.
        """
        self.click(self.COOKIE_BTN)

    # Localizador del botón "Join Today" para registrarse o unirse al sitio
    JOIN_BTN = (By.XPATH, "/html/body/ui-view/unauthenticated-container/div/div/unauthenticated-header-new/header/div/div[2]/ul/li[2]/a")

    def click_join_today(self):
        """
        Espera 5 segundos y luego hace clic en el botón "Join Today".
        Esta acción lleva al usuario al formulario de registro.
        """
        self.wait_seconds(5)
        self.click(self.JOIN_BTN)
