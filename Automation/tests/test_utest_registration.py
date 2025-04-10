# Importación de clases de páginas que representan cada paso del registro
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.location_page import LocationPage
from pages.devices_page import DevicesPage
from pages.final_registration_page import FinalRegistrationPage

def test_utest_registration(driver):
    """
    Flujo de la prueba:
    1. Abre el sitio web de uTest.
    2. Acepta las cookies.
    3. Hace clic en "Join Today" para iniciar el registro.
    4. Llena el formulario de datos básicos (nombre, correo, fecha de nacimiento).
    5. Hace clic en "Next".
    6. Continúa a través de la página de ubicación.
    7. Continúa a través de la página de dispositivos.
    8. Llena la contraseña, acepta términos y finaliza el registro.
    9. Verifica que el mensaje de bienvenida sea mostrado correctamente.

     driver: Instancia del WebDriver proporcionada por el framework de pruebas.
    """

    # Paso 1: Navegar al sitio uTest
    driver.get("https://www.utest.com/")

    # Paso 2: Aceptar cookies
    home = HomePage(driver)
    home.accept_cookies()

    # Paso 3: Clic en "Join Today"
    home.click_join_today()

    # Paso 4: Completar formulario de registro
    reg = RegistrationPage(driver)
    reg.fill_basic_info(
        first="Juan",
        last="Tester",
        email="juan.test123457@example.com",
        birth_month="May",
        birth_day="15",
        birth_year="1992"
    )
    reg.click_next()

    # Paso 5: Proceder con ubicación
    loc = LocationPage(driver)
    loc.proceed()

    # Paso 6: Proceder con dispositivos
    devices = DevicesPage(driver)
    devices.proceed()

    # Paso 7: Establecer contraseña y aceptar términos
    final = FinalRegistrationPage(driver)
    final.fill_password("HLeonardo++2")
    final.complete_registration()

    # Paso 8: Verificar mensaje de éxito
    assert final.verify_success_message(), "El mensaje de bienvenida no fue encontrado"
