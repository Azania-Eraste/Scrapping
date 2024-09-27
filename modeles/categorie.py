from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import os

class Categorie():
    def __init__(self,nom,url):

        options = Options()
        options.add_argument("--headless")
        options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

        script_dir = os.path.dirname(__file__)
        self.dir = os.path.join(os.getcwd(),'datas')
        geckodriver_path = os.path.join(script_dir, 'geckodriver.exe')
        service = Service(executable_path=geckodriver_path)
        self.driver = webdriver.Firefox(service=service, options=options)

        self.nom = nom
        self.url = url

        self.categoy_folder = os.path.join(self.dir,self.nom)



    def create_folder(self):

        if not os.path.exists(self.categoy_folder):
            os.makedirs(self.categoy_folder)



    def get_all_sub_categorie(self, selectorlink, selectorname):
        sub_categorie = []

        self.driver.get(self.url)

        while True:

            elements = self.driver.find_elements(By.CSS_SELECTOR, selectorlink)

            for element in elements:
                url = element.get_attribute('href')

                name_element = element.find_element(By.CSS_SELECTOR, selectorname)
                name = name_element.text

                if name:

                    sub_categorie.append({"name": name, "url": url})

            try:

                button = self.driver.find_element(By.CSS_SELECTOR, 'div.hugo4-pc-grid-scroll-inner div.hugo-dotelement.scroll-arrow.scroll-next')
                button.click() 

            except NoSuchElementException:
                break

        self.driver.quit()
        
        return sub_categorie
