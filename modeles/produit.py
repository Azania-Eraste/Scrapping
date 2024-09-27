import os
import csv
from urllib.parse import urljoin
import requests

class Produit():
    def __init__(self, nom, description, prix,img, sous_categorie):
        self.nom = nom
        self.description = description
        self.img = img
        self.prix = prix
        self.sous_categorie = sous_categorie
        self.categorie = sous_categorie.controler_categorie

        self.script_dir = os.path.dirname(__file__)
        categorie_folder = os.path.join(os.path.join(os.getcwd(),'datas'), self.categorie.nom)
        self.sub_category_folder = os.path.join(categorie_folder, self.sous_categorie.items["name"])
        self.image_folder = os.path.join(self.sub_category_folder, 'image')
        self.csv_path = os.path.join(self.sub_category_folder, 'data.csv')

    def save_product(self):
        """Enregistre les informations du produit dans un fichier CSV."""

        file_exists = os.path.exists(self.csv_path)

        with open(self.csv_path, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow(['name', 'price', 'description', 'image'])


            image_name = os.path.basename(self.img)  # Juste le nom de l'image, pas le chemin complet
            writer.writerow([self.nom, self.prix, self.description, image_name])

        print(f"Produit sauvegardé dans le fichier CSV : {self.csv_path}")



    def save_image(self):
        

        try:

            product_image_data = requests.get(self.img).content
            product_image_name = os.path.basename(self.img)
            product_image_path = os.path.join(self.image_folder, product_image_name)

            with open(product_image_path, 'wb') as img_file:
                img_file.write(product_image_data)
            
            print(f"Image téléchargée: {product_image_path}")

        except Exception as e:

            print(f"Erreur lors du téléchargement de l'image: {e}", )
            product_image_src = "Erreur lors du téléchargement"