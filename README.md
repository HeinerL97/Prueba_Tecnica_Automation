# Automatización del Registro en uTest.com

Este proyecto automatiza el flujo completo de registro de un nuevo usuario en el portal [uTest.com](https://www.utest.com), utilizando:

- **Selenium WebDriver**
- **Pytest**
- **Patrón de Diseño Page Object Model (POM)**
- **Python 3.x**

---

## Objetivo

Automatizar paso a paso el flujo de registro en uTest, validando los campos, botones, redirecciones y mensajes esperados para garantizar el correcto funcionamiento del proceso de creación de cuenta.

---

##  Matriz de Pruebas

| ID Caso | Nombre del Caso de Prueba                          | Precondiciones                        | Pasos                                                                 | Resultado Esperado                                                                 |
|---------|-----------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| CP_01   | Ingresar a la página                               | URL de la página                       | Abrir el navegador, ingresar la URL                                  | Se abre el navegador y también se carga la página de inicio                        |
| CP_02   | Aceptar cookies                                     | Página cargada correctamente           | Cargar utest.com, dar click en botón de cookies                      | Botón de cookies desaparece, permitiendo interacción con la página principal        |
| CP_03   | Ingresar al formulario de registro                  | Cookies aceptadas                      | Click en botón "Join Today" usando XPath especificado                | Redirección al formulario de registro                                               |
| CP_04   | Llenar formulario paso 1 – Datos personales         | En página de registro paso 1           | Ingresar First Name, Last Name, Email, Fecha de nacimiento           | Información ingresada correctamente y se habilita botón para continuar             |
| CP_05   | Selección correcta de fecha de nacimiento           | En formulario paso 1                   | Seleccionar mes, día y año del dropdown correctamente                | Fecha mostrada en campos seleccionados                                              |
| CP_06   | Continuar a paso 2 del registro                     | Campos paso 1 completados              | Click en botón “Next”                                                | Redirección a paso 2 del registro                                                   |
| CP_07   | Espera de carga en paso 2                           | Redirección a paso 2                   | Esperar 10 segundos hasta que el formulario esté visible             | Formulario paso 2 visible                                                           |
| CP_08   | Continuar a paso 3                                  | En formulario paso 2                   | Espera que se autocomplete la información y luego click en "Next"    | Redirección a paso 3                                                                |
| CP_09   | Espera de carga en paso 3                           | En paso 3                              | Esperar 10 segundos                                                   | Formulario paso 3 cargado                                                           |
| CP_10   | Ir al paso 4 del registro                           | En formulario paso 3                   | Esperar que se autocomplete la información y click en "Next"         | Redirección al formulario de contraseña                                             |
| CP_11   | Validar instrucciones de contraseña                 | En paso 4 del formulario               | Visualizar tooltip o instrucciones                                   | Instrucciones visibles y claras                                                     |
| CP_12   | Ingresar contraseña válida                          | En paso 4 del formulario               | Ingresar contraseña segura en campo "Password" y "Confirm password"  | Contraseña válida ingresada sin errores                                             |
| CP_13   | Seleccionar términos y políticas                    | En paso 4 del formulario               | Seleccionar los dos checkboxes requeridos                            | Ambos checkboxes seleccionados correctamente                                       |
| CP_14   | Finalizar registro                                  | Checkboxes marcados, password ok       | Click en botón de registro final y esperar carga                     | Redirección a pantalla de bienvenida                                                |
| CP_15   | Validar mensaje final de bienvenida                 | Registro exitoso                       | Verificar mensaje: “Welcome to the world's largest community…”       | Mensaje visible en la pantalla                                                     |
| CP_16   | Flujo completo de registro exitoso (end-to-end)     | Navegador abierto                      | Ejecutar pasos del CP_01 al CP_15 en orden                           | Registro completado y mensaje final validado                                       |
| CP_17   | Validar error por contraseña inválida               | En paso 4                              | Ingresar contraseña débil (solo números o < 10 caracteres)           | Aparece mensaje de error indicando contraseña no válida                            |
| CP_18   | Validar error si falta seleccionar algún checkbox   | En paso 4                              | Ingresar contraseña válida pero omitir check de aceptación           | Botón deshabilitado o error visible                                                 |
| CP_19   | Validar error si los campos obligatorios quedan vacíos | En cualquier paso de registro       | Dejar campos como Email o Nombre vacíos                              | Aparecen mensajes de error "Campo requerido"                                       |

---

### Autor

Desarrollado por Heiner Leonardo Urrego.
