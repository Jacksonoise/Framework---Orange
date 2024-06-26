import pytest
from Page.login_page import LoginPage
from selenium import webdriver

class TestLogin:
    def test_login_valido(self, driver: webdriver.Remote):
    # Inicializamos la página de inicio de sesión
        login_page = LoginPage(driver)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Realizamos el inicio de sesión
        login_page.login_completo("Admin", "admin123")
 

    def test_login_invalido(self, driver: webdriver.Remote):
    #   Inicializamos la página de inicio de sesión
            login_page = LoginPage(driver)
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

            #Realizamos el inicio de sesión
            login_page.login_invalido("Piripicho", "pipi123")


       


