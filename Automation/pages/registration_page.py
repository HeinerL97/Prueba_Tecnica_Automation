# Importa los localizadores necesarios para identificar elementos
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    """
    Representa la página de registro donde se ingresan los datos personales básicos del usuario.
    Hereda de BasePage para usar funciones reutilizables de Selenium.
    """

    # Localizadores de los campos de información básica
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    BIRTH_MONTH = (By.XPATH, '//select[@name="birthMonth"]')
    BIRTH_DAY = (By.XPATH, '//select[@name="birthDay"]')
    BIRTH_YEAR = (By.XPATH, '//select[@name="birthYear"]')

    def fill_basic_info(self, first, last, email, birth_month, birth_day, birth_year):
        """
        Llena el formulario de información básica con nombre, apellido, correo electrónico y fecha de nacimiento.

         first: Nombre del usuario
         last: Apellido del usuario
         email: Correo electrónico
         birth_month: Mes de nacimiento (visible en el dropdown)
         birth_day: Día de nacimiento (visible en el dropdown)
         birth_year: Año de nacimiento (visible en el dropdown)
        """
        self.send_keys(self.FIRST_NAME, first)
        self.send_keys(self.LAST_NAME, last)
        self.send_keys(self.EMAIL, email)
        self.select_dropdown_by_text(self.BIRTH_MONTH, birth_month)
        self.select_dropdown_by_text(self.BIRTH_DAY, birth_day)
        self.select_dropdown_by_text(self.BIRTH_YEAR, birth_year)

    # Localizador del botón para continuar al siguiente paso
    NEXT_BTN = (By.XPATH, '/html/body/ui-view/main/section/div/div[2]/div/div[2]/div/form/div[2]/button')

    def click_next(self):
        """
        Espera 5 segundos y luego hace clic en el botón "Next" para continuar con el proceso de registro.
        """
        self.wait_seconds(5)
        self.click(self.NEXT_BTN)
