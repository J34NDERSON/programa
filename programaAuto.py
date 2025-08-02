from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Fechar Chrome e chromedriver se estiverem abertos
os.system("taskkill /f /im chrome.exe >nul 2>&1")
os.system("taskkill /f /im chromedriver.exe >nul 2>&1")

# Configurar navegador
options = Options()
options.add_argument("--start-maximized")

# Iniciar navegador com ChromeDriver automático
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abrir site
navegador.get("https://www.google.com")
time.sleep(5)
navegador.quit()