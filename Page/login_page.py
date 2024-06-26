from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException


class LoginPage: 
    """
    Clase que contiene los elementos de la página de login
    """
    def __init__(self, driver: webdriver.Remote, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time


    def esperar_por_los_elementos(self, locator):
        try:
            wait = WebDriverWait(self.driver, self.wait_time)
            element = wait.until(EC.presence_of_element_located(locator))
            element = wait.until(EC.visibility_of(element))
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except (TimeoutException, NoSuchElementException, ElementNotInteractableException) as e:
            print(f"Error al encontrar el elemento {locator}: {e}")
            return None

    @property
    def __input_username(self):
        return self.esperar_por_los_elementos((By.XPATH, "//input[contains(@class, 'oxd-input')][@name='username']"))
    
    @property
    def __input_password(self):
        return self.esperar_por_los_elementos((By.XPATH, "//input[@type='password' and @name='password']"))
    
    @property
    def __button_login(self):
        return self.esperar_por_los_elementos((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button"))
    
    
    @property
    def __credential_error(self):
        try:
            element = self.esperar_por_los_elementos((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
            return element.text if element else None
        except NoSuchElementException:
            return None
    

    def login_completo(self, username, password):
        """
        Metodo que se encarga de realizar el login completo
        args:
        Username: Nombre de usuario 
        Password: Contraseña 
        """
        
        self.__input_username.send_keys(username)
        self.__input_password.send_keys(password)
        self.__button_login.click()

        if "dashboard" in self.driver.current_url:
            print("Inicio de sesión exitoso.")
        else:
            print("Error al iniciar sesión. Verifica tus credenciales.")

             # Verificación 2: Comprobar si se muestra un mensaje de error
        try:
            error_message = self.__credential_error
            if error_message:
             print(f"Mensaje de error: {error_message}")
            
        except NoSuchElementException:
         pass  # No se encontró el mensaje de error, lo cual es correcto


    def login_invalido(self, username, password):
        """
        Método que intenta realizar un inicio de sesión inválido para verificar el mensaje de error.
        Args:
            username (str): Nombre de usuario inválido
            password (str): Contraseña inválida
        """
        self.__input_username.send_keys(username)
        self.__input_password.send_keys(password)
        self.__button_login.click()

        try:
            # Esperar a que aparezca el mensaje de error de credenciales
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
            )
            print(f"Mensaje de error de credenciales: {error_message.text}")
        
        except TimeoutException:
            print("No se encontró el mensaje de error de credenciales.")
    

    
   
    

     
    