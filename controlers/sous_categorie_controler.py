from modeles.sous_categorie import SousCategorie

class SousCategorieControler():
    def __init__(self, items, controler_categorie):
        self.items = items
        self.controler_categorie = controler_categorie

    def sous_categorie_scrapper(self):
        sous_categorie = SousCategorie(self.items["name"],self.items["url"], self.controler_categorie)

        sous_categorie.create_folder()

        sous_categorie.create_image_folder()

        product = sous_categorie.get_all_product()

        return product

