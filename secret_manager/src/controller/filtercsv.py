import csv


def filter_blanks(filename):
    
    try:
        data = []
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                flag = True
                for i in row:
                    if i.strip() == '':
                        flag = False
                if flag:
                    data.append(row)
                    
    finally:
        
        with open(filename, "w") as file:
            for line in data:
                file.write(f"{line}\n")

filename = str(input())


'''def count_gen(data):
    
    result = {}

    for i in data:
        if result.get(i[2]):
            result[i[2]] += 1
        else:
            result[i[2]] = 1

    return result'''