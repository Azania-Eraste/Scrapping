from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os
from urllib.parse import urljoin



class SousCategorie():
    def __init__(self,nom,url,categorie):
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
        self.categorie = categorie

        categorie_folder = os.path.join(self.dir, self.categorie.nom)
        self.sub_category_folder = os.path.join(categorie_folder, self.nom)
        self.image_folder = os.path.join(self.sub_category_folder, 'image')

    def create_folder(self):
        """
        The function creates a folder for a sub-category within a category if it does not already exist.
        """
        if not os.path.exists(self.sub_category_folder):
            os.makedirs(self.sub_category_folder)

    def create_image_folder(self):


        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

    def get_all_product(self):
        """
        The function `get_all_product` retrieves product information from a web page using CSS selectors
        and stores it in a list.
        """
        self.driver.get(self.url)



        product_list = []

        products = self.driver.find_elements(By.CSS_SELECTOR, "div.organic-list.app-organic-search-mb-20.viewtype-gallery div.fy23-search-card.m-gallery-product-item-v2.J-search-card-wrapper.fy23-gallery-card.searchx-offer-item")

        for product in products:

            product_image = product.find_element(By.CSS_SELECTOR, "div.search-card-m-imgarea.gallery-card-layout__img div.search-card-e-slider div.search-card-e-slider__wrapper a.search-card-e-slider__link.search-card-e-slider__gallery img")

            product_image_src = product_image.get_attribute('src')

            product_image_src = urljoin(self.url, product_image_src)

            product_info = product.find_element(By.CSS_SELECTOR, "div.search-card-info__wrapper")

            product_name = product_info.find_element(By.CSS_SELECTOR, "div.card-info.gallery-card-layout-info h2.search-card-e-title a span")


            product_price = product_info.find_element(By.CSS_SELECTOR, "div.card-info.gallery-card-layout-info a div.search-card-e-price-normal.margin-bottom-4 div.search-card-e-price-main")


            product_description = product_info.find_element(By.CSS_SELECTOR, "div.card-info.gallery-card-layout-info a.search-card-e-detail-wrapper.gallery-card-info__sales")


            product_list.append({"name" : product_name.text, "price" : product_price.text, "description" : product_description.text, "image" : product_image_src})

            print(f'Nom : {product_name.text}\nPrice : {product_price.text}\nDescription : {product_description.text} \nImage : {product_image_src}\n')

        self.driver.quit()
        
        return product_list


