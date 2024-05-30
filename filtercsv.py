import csv


def filter_blanks():
    
    with open('fileimport.csv', 'r', newline='', encoding='utf-8') as file1, \
         open('file.csv', 'a', newline='', encoding='utf-8') as file2:
        
        reader = csv.reader(file1)
        writer = csv.writer(file2)
        
        for row in reader:
            if len(row) == 3 and all(row):  
                writer.writerow(row)


def read_csv_file(filename):

    try:
        result = []
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.DictReader(csvfile)
            for row in spamreader:
                result.append(dict(row))
    finally:
        return result
    

def add_item(diccionario):
    
    with open('file.csv', 'r', newline='', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        encabezados = lector_csv.fieldnames

    with open('file.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor_csv.writerow(diccionario)
