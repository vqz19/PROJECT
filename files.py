import csv


def create_json_file(filename):
    ...
    

def create_file(filename, ext, mode, data):

    """create a file
        ARG:  - filename (str): the filename
              - ext (str): the file extension
              - mode (str): append (a), write (w), read (r)
    """

    with open(f"{filename}.{ext}") as file:
        for line in data:
            file.write(f"{line}\n")


def read_csv_file(filename):

    try:
        result = []
        with open(filename) as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                result.append(row)
    finally:
        return result


def count_gen(data):
    
    result = {}

    for i in data:
        if result.get(i[2]):
            result[i[2]] += 1
        else:
            result[i[2]] = 1

    return result



data = [
    "NOMBRE,EDAD,SEXO,CURSO,GANO",
    "alan,20,F,intro,false",
    "samuel,18, ,intro,true",
    "karen,18,F,intro,false",
    "isabella,40,M,intro,false",
    "antonia,20,F,intro,true"
]



create_file("personas_pasar_intro","csv","w", data)
data = read_csv_file("personas_pasar_intro.csv")
print(data)
print(count_gen(data))
print(data)