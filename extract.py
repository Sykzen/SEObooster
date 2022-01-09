import os
import numpy as np
import pandas as pd
import re
from collections import Counter

product=pd.read_excel('product.xlsx')
nb_rows,nb_columns=product.shape[0],product.shape[1]

def chgetInfo():
    return product.columns
def chget(val):   
    return {_:product[_][val] for _ in product.columns}
product_nbr=[i for i in range(nb_rows) if not np.isnan(chget(i)["Image Position"]) and chget(i)["Image Position"]==1]

class Product:
    def __init__(self,number):
        val=chget(number)
        self.handle=val["Handle"]
        self.title=val["Title"]
        self.desc=val["Body (HTML)"]
        self.brand=val["Vendor"]
        self.standard=val["Standard Product Type"]
        self.custom=val["Custom Product Type"]
        self.tags=val["Tags"]
        self.published=val["Published"]
        self.name1=val["Option1 Name"]
        self.name2=val["Option1 Value"]
        self.imgpos=val["Image Position"]
        
        
    def getMaxInfo(self):
        dicte={}
        dicte["Genre"]=["Femme","Homme","Unisexe"][2 if ("Mixte" or "mixte" or "Unisexe" in self.title) else ("Homme" or "homme" in self.title)]
        last_part_in_title=self.title.split('-')[-1]
        keyword=last_part_in_title.split(" ")
        #dicte["Contenance"]=
        #dicte["Ingrédients"]=
       # dicte["Object"]=
    def typeproducte(self):
        def probablyCoffretParfum(title):
            if self.title.count("ml")>=2:
                return True
            if self.title.count("+")>=1:
                return True
            if "parfum" in self.title:
                return True
        def probablyKitCheveux(title):
            if self.title.count("ml")>=2:
                return True
            if self.title.count("+")>=1:
                return True
            if ("masque" or "botox" or "shampoing" or "lifting") in self.title:
                return True
        if "parfum" or "Parfum" in self.title and not probablyCoffretParfum(self.title):
            return "Santé et beauté > Hygiène personnelle > Cosmétiques > Parfums et eaux de Cologne"
        if ("déodorant"or "Déodorant") in self.title:
            return "Santé et beauté > Hygiène personnelle > Déodorants et anti-transpirants > Déodorant"
        if probablyCoffretParfum(self.title):
            return "Santé et beauté > Hygiène personnelle > Cosmétiques > Kits de cosmétiques"
        if ("Lait" or "Lotions" or "Crème") and not probablyCoffretParfum(self.title):
            return "Santé et beauté > Hygiène personnelle > Cosmétiques > Soin de la peau > Crèmes et lotions"
        if probablyKitCheveux(self.title):
            return "Santé et beauté > Hygiène personnelle > Soin des cheveux > Kits de soin des cheveux"
        if ("Masque" or "Botox" or "Shampoing" or "Lifting") in self.title:
            return "Santé et beauté > Hygiène personnelle > Soin des cheveux"
    def procTags(self):
        list_of_tags=[]
        liste_type=self.typeproducte().split(">")
        for i in liste_type:                
            list_of_tags.append(i)
        list_of_tags.append(self.brand)
        return list_of_tags
def procUselessKeyword():
        l=[]
        for i in product_nbr:
            for k in list(filter(None,re.split("[ -]",Product(i).title))):
                l.append(k)
        return Counter(l)
procUselessKeyword()
    