from dbfread import DBF

table = DBF("Habitats_Infrastructure_Lines_2425.dbf")
for record in table:
    for field, value in record.items():
        if "POM24001" in str(value):
            print("Column name:", field)
            break