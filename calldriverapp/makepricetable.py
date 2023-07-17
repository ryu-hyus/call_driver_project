from calldriverapp.models.pricefile import PriceFile

pf = PriceFile()
pf.file = "./calldriverapp/uploads/fare_table.csv"
pf.save()