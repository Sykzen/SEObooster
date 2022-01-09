import openpyxl
import re
import pathlib
import pandas as pd
import random
import numpy as np
import math
from extract import *
Analyse={"Error Image Not found": [],"Error Title no well formulate":[],
         "Error marque dans le titre et distributeur":[],"Error Copie in": [],"to Adjust Stand empty or wrong":[]}
list_of_brand=[]



    
def AnalyseCopie():
    for i in product_nbr:
        if Product(i).handle[0:5]=="copie":
            Analyse["Error Copie in"].append(i)
def AnalyseWellFormulateStandard():
    for i in product_nbr:
        prod=Product(i)
        typeproduct=prod.typeproducte()
        if typeproduct!=prod.standard or (not type(prod.custom)==str and np.isnan(prod.custom)):
            Analyse["to Adjust Stand empty or wrong"].append(i)
def AnalyseTitle():
    for i in product_nbr:
        if not '-' in Product(i).title:
                Analyse["Error Title no well formulate"].append(i)
            
    
def AnalyseImage():
    for i in product_nbr:
        if np.isnan(Product(i).imgpos):
            Analyse["Error Image Not found"].append(i)
def getBrand():
    for i in iter(product_nbr):
        prod=Product(i)
        if '-' not in prod.title:
            continue
        if type(prod.title) is float or type(prod.brand) is float:
            Analyse.append("Error empty case " + str(i))
        else:
            brand=prod.title[:prod.title.index('-')-1]
            vendor=prod.brand
            if vendor != brand:
                Analyse["Error marque dans le titre et distributeur"].append(i)
            list_of_brand.append(brand)
            list_of_brand.append(vendor)
def AnalyseCatalogue():
    AnalyseImage()
    AnalyseTitle()
    AnalyseWellFormulateStandard()
    AnalyseCopie()
    getBrand()
    brandl=set(list_of_brand)
AnalyseCatalogue()
