# Importa los localizadores para elementos web (por XPATH, ID, etc.)
from selenium.webdriver.common.by import By

# Importa la clase base con funcionalidades reutilizables como click y wait
from pages.base_page import BasePage

class LocationPage(BasePage):
    """
    Representa la página de ubicación (Location) dentro del flujo de registro o navegación.
    Hereda de BasePage para reutilizar métodos de interacción con la interfaz.
    """

    # Localizador del botón "Siguiente" (Next) para avanzar al siguiente paso del proceso
    NEXT_BTN = (By.XPATH, '/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/div/button')

    def proceed(self):
        """
        Espera 5 segundos y hace clic en el botón 'Siguiente'.
        Esta acción avanza al usuario al próximo paso del formulario o proceso.
        """
        self.wait_seconds(5)
        self.click(self.NEXT_BTN)
