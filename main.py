from lifestore_file import lifestore_sales, lifestore_products, lifestore_searches

"""lifestore_searches = [id_search, id product] 

lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)] 

lifestore_products = [id_product, name, price, category, stock]"""

#login
def login():
    access = False
    intentos = 0
    
    bienvenida = "¡Bienvenido(a) a LifeStore!\nIngresa con tus credenciales"
    print(bienvenida)
    
    while not access:
      usuario = input('Usuario: ')
      contra = input('Clave secreta: ')
      intentos += 1
      if usuario == 'Jimmy' and contra == 'MasterPro':
        access = True
        print('¡Bienvenido al informe anual de rotación de productos!')
      else:
        print('Tienes', 3 - intentos, 'intentos restantes')
        if usuario == 'Jimmy':
          print('Clave secreta incorrecta')
        else:
          print(f'El usuario: "{usuario}" no esta registrado, intenta de nuevo')
    
    if intentos == 3:
      exit()


def best_products():
    prod_reviews = {}
    for sale in lifestore_sales:
        #determinación de producto y su review de venta
        prod_id = sale[1]
        review = sale[2]
        #categorización por id de producto
        if prod_id not in prod_reviews.keys():
            prod_reviews[prod_id] = []
        prod_reviews[prod_id].append(review)

    id_rev_prom = {}
    for id, reviews in prod_reviews.items():
        #determinación de promedio de las reviews
        rev_prom = sum(reviews) / len(reviews)
        rev_prom = int(rev_prom*100)/100
        id_rev_prom[id] = [rev_prom, len(reviews)]

    dicc_en_list = []
    for id, lista in id_rev_prom.items():
        #ordenación de la lista
        rev_prom = lista[0]
        cant = lista[1]
        sub = [id, rev_prom, cant]
        dicc_en_list.append(sub)

    def seg_elemnto(sub):
      return sub[1]

    dicc_en_list = sorted(dicc_en_list, key=seg_elemnto, reverse=True)
    
    for sublista in dicc_en_list[:5]:
        id, rev, num = sublista
        indice_lifestp = id - 1
        prod = lifestore_products[indice_lifestp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        print(
            f'El producto "{nombre}" tiene:\n\tReview promedio: {rev},\n\tNúmero de ventas: {num}')

def bad_products():
    prod_reviews = {}
    for sale in lifestore_sales:
        #determinación de producto y su review de venta
        prod_id = sale[1]
        review = sale[2]
        #categorización por id de producto
        if prod_id not in prod_reviews.keys():
            prod_reviews[prod_id] = []
        prod_reviews[prod_id].append(review)

    id_rev_prom = {}
    for id, reviews in prod_reviews.items():
        #determinación de promedio de las reviews
        rev_prom = sum(reviews) / len(reviews)
        rev_prom = int(rev_prom*100)/100
        id_rev_prom[id] = [rev_prom, len(reviews)]

    dicc_en_list = []
    for id, lista in id_rev_prom.items():
        #ordenación de la lista
        rev_prom = lista[0]
        cant = lista[1]
        sub = [id, rev_prom, cant]
        dicc_en_list.append(sub)

    def seg_elemnto(sub):
      return sub[1]

    dicc_en_list = sorted(dicc_en_list, key=seg_elemnto, reverse=True)
    
    for sublista in dicc_en_list[-5:]:
        id, rev, num = sublista
        indice_lifestp = id - 1
        prod = lifestore_products[indice_lifestp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        print(f'El producto "{nombre}" tiene:\n\tReview promedio: {rev},\n\tNúmero de ventas: {num}')


def mensuales():
    id_categoria = [ [product[0], product[3]] for product in lifestore_products]

    productos_clasificados = {}
    for par in id_categoria:
      id = par[0]
      cat = par[1]
      if cat not in productos_clasificados.keys():
        productos_clasificados[cat] = []
      productos_clasificados[cat].append(id)

    #print(productos_clasificados["procesadores"])

    #ventas de cada mes
    id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0]

    categorizacion_meses = {}

    for par in id_fecha:
      id = par[0]
      _, mes, _ = par[1].split('/')
      if mes not in categorizacion_meses.keys():
        categorizacion_meses[mes] = []
      categorizacion_meses[mes].append(id)

    #suma del total de las ventas por mes
    for key in categorizacion_meses.keys():
      lista_mes = categorizacion_meses[key]
      suma_venta = 0
      for id_venta in lista_mes:
        indice = id_venta - 1
        info_venta = lifestore_sales[indice]
        id_producto = info_venta[1]
        precio = lifestore_products[id_producto - 1] [2]
        suma_venta += precio
      print(key,suma_venta, f'ventas totales: {len(lista_mes)}')


def menu():
    login()
    while True:
        print('\t¿Que información deseas conocer?:')
        print('\t1. Reviews de los mejores productos')
        print('\t2. Reviews más bajos')
        print('\t3. Productos más vendidos')
        print('\t4. Productos menos vendidos')
        print('\t5. Productos más buscados')
        print('\t6. Productos menos buscados')
        print('\t7. Ventas mensuales')
        print('\t8. Ventas totales del ejercicio')

        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            best_products()
        elif seleccion == '2':
          bad_products()
        elif seleccion == '8':
          categoria()
          print('\n')
        elif seleccion == '0':
            exit('Gracias por tu visita, ¡vuelve pronto!')
        else:
            print('¡Elige una opción enlistada!')

menu()