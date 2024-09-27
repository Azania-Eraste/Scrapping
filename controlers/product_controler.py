from modeles.produit import Produit

class ProductControler():
    def __init__(self, product, sous_categorie_controler):
        self.product = product
        self.sous_categorie_controler = sous_categorie_controler

    def produit_scrapper(self):
        
        product = Produit(self.product["name"], self.product["description"], self.product["price"], self.product["image"], self.sous_categorie_controler)

        product.save_image()

        product.save_product()

