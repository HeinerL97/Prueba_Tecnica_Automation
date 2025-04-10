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

| ID Caso | Nombre del Caso de Prueba                           | Precondiciones              | Pasos                                                                                 | Resultado Esperado                                                                 |
|---------|------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| TC_01   | Aceptar cookies                                      | Página cargada correctamente| Cargar utest.com, dar click en botón de cookies                                       | Botón desaparece, se habilita la navegación                                       |
| TC_02   | Ingresar al formulario de registro                   | Cookies aceptadas           | Click en botón "Join Today" usando XPath especificado                                 | Redirección a paso 1 del formulario de registro                                   |
| TC_03   | Llenar formulario paso 1 – Datos personales          | En página de registro paso 1| Ingresar First Name, Last Name, Email, Fecha de nacimiento                            | Campos correctamente diligenciados                                                |
| TC_04   | Selección correcta de fecha de nacimiento            | En formulario paso 1        | Seleccionar mes, día y año del dropdown                                               | Fecha mostrada en campos seleccionados                                            |
| TC_05   | Continuar a paso 2 del registro                      | Campos paso 1 completados   | Click en botón “Next”                                                                 | Redirección a paso 2 del registro                                                 |
| TC_06   | Espera de carga en paso 2                            | Redirección a paso 2        | Esperar 10 segundos                                                                   | Formulario paso 2 visible                                                         |
| TC_07   | Continuar a paso 3                                   | En formulario paso 2        | Click en botón "Next"                                                                 | Redirección a paso 3                                                              |
| TC_08   | Espera de carga en paso 3                            | En paso 3                   | Esperar 10 segundos                                                                   | Formulario paso 3 cargado                                                         |
| TC_09   | Ir al paso 4 del registro                            | En formulario paso 3        | Click en botón "Next"                                                                 | Redirección al formulario de contraseña                                           |
| TC_10   | Validar instrucciones de contraseña                  | En paso 4                   | Visualizar instrucciones                                                              | Instrucciones visibles y claras                                                   |
| TC_11   | Ingresar contraseña válida                           | En paso 4                   | Ingresar contraseña segura en "Password" y "Confirm password"                        | Contraseña válida ingresada sin errores                                           |
| TC_12   | Seleccionar términos y políticas                     | En paso 4                   | Seleccionar los dos checkboxes requeridos                                             | Ambos checkboxes seleccionados correctamente                                      |
| TC_13   | Finalizar registro                                   | Checkboxes y contraseña ok  | Click en botón de registro final                                                      | Redirección a pantalla de bienvenida                                              |
| TC_14   | Validar mensaje final de bienvenida                  | Registro exitoso            | Verificar mensaje: “Welcome to the world's largest community…”                        | Mensaje visible en la pantalla                                                    |
| TC_15   | Flujo completo de registro exitoso (end-to-end)      | Navegador abierto           | Ejecutar pasos TC_01 a TC_14                                                          | Registro completado y mensaje validado                                            |
| TC_16   | Validar error por contraseña inválida                | En paso 4                   | Ingresar contraseña débil                                                             | Aparece mensaje de error de contraseña                                            |
| TC_17   | Validar error si falta seleccionar algún checkbox    | En paso 4                   | Ingresar contraseña válida pero omitir check de aceptación                            | Error visible o botón deshabilitado                                               |
| TC_18   | Validar error si los campos obligatorios quedan vacíos| En cualquier paso           | Dejar campos como Email o Nombre vacíos                                               | Mensaje de error "Campo requerido"                                                |
