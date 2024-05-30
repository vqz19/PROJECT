import random

def main():

    nums = [1,2]

    answer = int(input('''escribe (1) si quieres probar una contraseña
escribe (2) si quieres que te generemos una contraseña
RESPUESTA: '''))
    while answer not in nums:
        print("RESPUESTA NO VALIDA")
        answer = int(input("escribe (1) si quieres probar una contraseña"
                   "escribe (2) si quieres que te generemos una contraseña"))
    
    if answer == 1:
        proof_pass()
    elif answer == 2:
        password = gen_pass()
        print("----------------------------------------------")
        print(f"TU CONTRASEÑA CREADA ES: {password}")
        print("----------------------------------------------")

def gen_pass():
    
    abc = "abcdefghijklmnñopqrstuvwxyz"
    abcmayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "0123456789"
    specs = ".,!+_-/%<;"

    conjunt = f"{abc}{nums}{abcmayus}{specs}"
    create_pass = random.sample(conjunt, 9)
    password = "".join(create_pass)

    return password






def proof_pass():

    print("----------------------------------------------")
    pas = input("ESCRIBE TU CONSTRASEÑA: ")
    print("----------------------------------------------")

    chars, mayus, minus, num, spec = proof(pas)

    if not chars:
        print("LA CONTRASEÑA DEBE TENER ALMENOS 8 CARACTERES")
        proof_pass()
    elif not mayus:
        print("LA CONTRASEÑA DEBE TENER AL MENOS UNA MAYUSCULA")
        proof_pass()
    elif not minus:
        print("LA CONTRASEÑA DEBE TENER ALMENOS UNA MINUSCULA")
        proof_pass()
    elif not num:
        print("LA CONTRASEÑA DEBE TENER ALMENOS UN NUMERO")
        proof_pass()
    elif not spec:
        print("LA CONTRASEÑA DEBE TENER AL MENOS UN CARACTER ESPECIAL")
        proof_pass()
    else:
        print("----------------------------------------------")
        print(f"LA CONTRASEÑA ({pas}) ES PERMITIDA")
        print("----------------------------------------------")
    


def proof(pas):

    chars = False
    mayus = False
    minus = False
    num = False
    spec = False

    acum = 0 
    for i in pas:
        acum += 1
    
    if acum >= 8:
        chars = True

    for i in pas:
        if i.isupper():
            mayus = True
        elif i.islower():
            minus = True
        elif i.isdigit():
            num = True
        else:
            spec = True
    
    return chars, mayus, minus, num, spec


main()