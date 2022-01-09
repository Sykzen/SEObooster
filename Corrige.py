from Analyse import *
path =str(pathlib.Path(__file__).parent.absolute())+'\product.xlsx'
wb_obj = openpyxl.load_workbook(path.strip())
sheet_obj = wb_obj.active
def CorrigeStandard():
    for i in Analyse["to Adjust Stand empty or wrong"]:
        custom=sheet_obj.cell(row=i+2,column=6)
        standard=sheet_obj.cell(row=i+2,column=5)
        standard.value=Producte(i).title
        custom.value=np.nan
    
def CorrigeCopie():
    for i in Analyse["Error Copie in"]:
        HandleVal=sheet_obj.cell(row=i+2,column=1)
        HandleVal.value=Producte(i).handle[9:]
def CorrigeBrand():
    for i in Analyse['Error marque dans le titre et distributeur']:
        prod=Producte(i)
        title=prod.title
        if prod.brand in brand:
            truebrand=prod.brand
        elif title[:title.index('-')-1] in brand:
            truebrand=title[:title.index('-')-1]
        vendor=sheet_obj.cell(row=i+2,column=4)
        vendor.value=truebrand
        Title=sheet_obj.cell(row=i+2,column=2)
        Title.value=truebrand+ " -" + title[title.index('-')+1:]
        
def Correction():
    CorrigeBrand()
    CorrigeCopie()
    CorrigeStandard()
    wb_obj.save('product.xlsx')
Correction()
        