# Importación del localizador de elementos por diferentes métodos (ID, XPATH, etc.)
from selenium.webdriver.common.by import By

# Importación de la clase base que contiene métodos reutilizables como click, send_keys, wait, etc.
from pages.base_page import BasePage

class FinalRegistrationPage(BasePage):
    """
    Representa la página final del proceso de registro en la aplicación.
    Hereda de BasePage para usar funcionalidades comunes de automatización.
    """

    # Localizadores de los elementos del formulario de registro final
    PASSWORD = (By.ID, "password")  # Campo para ingresar la contraseña
    CONFIRM_PASSWORD = (By.ID, "confirmPassword")  # Campo para confirmar la contraseña
    CHECKBOX1 = (By.XPATH, '/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]')  # Primer checkbox de aceptación
    CHECKBOX2 = (By.XPATH, '/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]')  # Segundo checkbox de aceptación
    COMPLETE_BTN = (By.ID, "laddaBtn")  # Botón para completar el registro
    WELCOME_MSG = (By.XPATH, '/html/body/ui-view/unauthenticated-container/div/div/div/ui-view/main/div/div/div[1]/div/h1')  # Mensaje de bienvenida

    def fill_password(self, password):
        """
        Llena los campos de contraseña y confirma la contraseña, además de seleccionar los checkbox requeridos.

        :param password: La contraseña que se desea establecer.
        """
        self.send_keys(self.PASSWORD, password)
        self.send_keys(self.CONFIRM_PASSWORD, password)
        self.click(self.CHECKBOX1)
        self.click(self.CHECKBOX2)

    def complete_registration(self):
        """
        Hace clic en el botón para completar el proceso de registro.
        """
        self.click(self.COMPLETE_BTN)

    def verify_success_message(self):
        """
        Verifica si el mensaje de bienvenida aparece después del registro exitoso.

        return: True si el mensaje esperado está presente en la página, False en caso contrario.
        """
        self.wait_seconds(10)  # Espera para asegurar que la página haya cargado completamente
        return "Welcome to the world's largest community of freelance software testers!" in self.get_text(self.WELCOME_MSG)
