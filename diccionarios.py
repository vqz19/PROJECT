
shop = {
    "sports": {
        "ball": 3,
        "golf ball": 20,
        "golf club": 4,
    },
    "clothes": {
        "t-shirt": 8,
        "skirt": 10
    },
    "toys": {
        "ken": 40,
        "holly toy": 80,
        "barbie": 69
    },
    "techonlogy": {
        "phone": 5,
        "computer": 10,
        "smartphone": 70
    }
}

'''print(shop)

print(shop["sports"])

print(shop["techonlogy"]["computer"])'''


def add_product(new_product, category, quantity=None, *args, **kwargs):
    print(new_product, category, quantity, args, kwargs)


add_product("tanga brasilera", "sports")
add_product("br***5000", "toys")
add_product("smartwhatch", "technology", 800000)

add_product(quantity=100,
            new_product="luxury",
            category="clothes")

add_product("bread",
            category="bakery")

'''add_product(category="cooking",  # UNA VEZ SE EMPEIZA DEFINIR, DEBE SEGUIR DEFINIENDOSE
            "chocolate")'''

add_product(category="bakery",
            new_product="bread",         #cuando hay un parametro nuevo que se define, se guarda en **kwargs como diccionario
            lover="CR7")

x = [0,1,2,3,4]


product = {
    "category": "sports",
    "new_product": "ball",
    "quantity": 9,                 # SE DESEMPAQUETA EL DICCIONARIO, CON LOS PARAMETROS YA ASIGNADOS EN ESTE, Y SE ENTREGA DECONSTRUIDO A LA FUNCION
    
}

add_product(args=x,**product)

add_product("arroz","comida",9,1,2,3,4,5,
            lover = "CR7")


'''"value1": 1,
    "value2": 2'''




def add_product2(catalog, product, category, quantity):

    try:
        if not catalog.get(category):
            raise Exception(f"The category {category} does not exist")
        
        if catalog[category].get(product, None) != None:
            raise Exception(f"The product {product} already exist in {category}")

        catalog[category][product] = quantity
    except Exception as ex:
        print(ex)
    finally:
        print(f"The action to made was: ({product}, {category}, {quantity})")








shop = {
    "sports": {
        "ball": 3,
        "golf ball": 20,
        "golf club": 4,
    },
    "clothes": {
        "t-shirt": 8,
        "skirt": 10
    },
    "toys": {
        "ken": 40,
        "holly toy": 80,
        "barbie": 69
    },
    "techonlogy": {
        "phone": 5,
        "computer": 10,
        "smartphone": 70
    }
}


def add_product(shop, new_product, category, quantity=0):


    if category in shop:
        if new_product in shop[category]:
            print("el producto ya está en el catalogo")
        else:
            shop[category][new_product] = quantity

    ...

def buyitem(shop,product):

    for i in shop:
        if product in shop[i]:
            if shop[i][product] == 0:
                print("no quedan mas unidades de este producto")
            else:
                shop[i][product] -= 1
    else:
        print("el producto no está disponible")
    ...





#add_product(shop, "pelota", "sports", 10)
buyitem(shop,"ball")
buyitem(shop,"ball")
buyitem(shop,"ball")
buyitem(shop,"ball")
print(shop)
