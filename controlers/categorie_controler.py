from modeles.categorie import Categorie

class CategorieControler():
    def __init__(self, url, nom):
        self.url = url
        self.nom = nom
    
    def categorie_scrappers(self):
        categorie = Categorie(self.nom, self.url)

        categorie.create_folder()

        items = categorie.get_all_sub_categorie('a.hugo-dotelement.leaf-nav-item', 'div.item-title.hugo3-util-ellipsis.line-2')

        for item in items:

            print(item)

        return items
