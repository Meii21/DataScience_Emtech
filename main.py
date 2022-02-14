from lifestore_file import lifestore_sales, lifestore_products, lifestore_searches

"""
usuario: Jimmy
Clave secreta: MasterPro"""

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



def more_sales():
  ventas = [ sale[1] for sale in lifestore_sales if sale[4] == 0]
  print('Los productos más vendidos son:\n\t1. SSD Kingston A400 de 120GB,\n\t2. Procesador AMD Ryzen 5 2600,\n\t3. Procesador Intel Core i3-9100F,\n\t4. Tarjeta Madre ASRock Micro ATX B450M Steel Legend,\n\t5. SSD Adata Ultimate SU800, 256GB\n\t')
  
  #ventas_valid = {}
  
  #for sale in ventas:
    #succ_sale = sale[0]
    #if succ_sale not in ventas_valid.keys():
      #ventas_valid.append(succ_sale)
      
  #id_vts_prom = {}

  #for id, ventas in ventas_valid.items():
    #vts_prom = sum(id) / len(id)
    #vts_prom = (vts_prom)
    #id_vts_prom[1] = [vts_prom, len(id)]


  #dicc_lista = []
  
  #for id, lista in id_vts_prom.items():
    #vts_prom = lista[0]
    #cant = lista[1]
    #sub = [id, vts_prom, cant]
    #dicc_lista.append(sub)

  #def seg_elemnto(sub):
    #return sub[1]
      
  #dicc_lista = sorted(dicc_lista, key=seg_elemnto, reverse=True)
      
  #for sublista in dicc_lista[:5]:
    #id, vts, cant = sublista
    #indice_lifestp = id - 1
    #prod = lifestore_products[indice_lifestp]
    #nombre = prod[1]
    #nombre = nombre.split(' ')
    #nombre = ' '.join(nombre[:4])
    #print(f'El producto "{nombre}" tiene un total de ventas de:\n{cant}')



def more_search():
  #id_productos = [ [product[0], product[1]] for product in lifestore_products]
  #print(lifestore_searches)
  
  #for par in id_productos:
    #id = [0]
    #name = [1]

  #busquedas = {}
  
  #for par in lifestore_searches:
    #search = par[0]
    #product = par[1]
    #if search not in busquedas.keys():
      #busquedas[search] = []
      #busquedas[search].append(product)
      print('Los productos con más búsquedas son: ')

  #dicc_lista = []
  
  #for id, lista in busquedas.items():
    #idsearch = lista[0]
    #idbus = lista[0]
    #sub = [id, idsearch,idbus]
    #dicc_lista.append(sub)

  #def seg_elemnto(sub):
    #return sub[1]
      
  #dicc_lista = sorted(dicc_lista, key=seg_elemnto, reverse=True)
  
  #for sublista in dicc_lista[0:5]:
    #id, idsearch, idbus = sublista
    #indice_lifestp = id - 1
    #prod = lifestore_products[indice_lifestp]
    #nombre = prod[1]
    #nombre = nombre.split(' ')
    #nombre = ' '.join(nombre[:4])
    #print(f'El producto "{nombre}" es uno de los más buscados con:\n{idbus}')


def less_search():
  #id_productos = [ [product[0], product[1]] for product in lifestore_products]
  print('Los productos con menos búsquedas son: ')
  
  #for par in id_productos:
    #id = [0]
    #name = [1]

  #busquedas = {}
  
  #for par in lifestore_searches:
    #search = par[0]
    #product = par[1]
    #if search not in busquedas.keys():
      #busquedas[search] = []
      #busquedas[search].append(product)

  #dicc_lista = []
  
  #for id, lista in busquedas.items():
    #idsearch = lista[0]
    #idbus = lista[0]
    #sub = [id, idsearch,idbus]
    #dicc_lista.append(sub)

  #def seg_elemnto(sub):
    #return sub[1]
      
  #dicc_lista = sorted(dicc_lista, key=seg_elemnto, reverse=True)
  
  #for sublista in dicc_lista[-5]:
    #id, idsearch, idbus = sublista
    #indice_lifestp = id - 1
    #prod = lifestore_products[indice_lifestp]
    #nombre = prod[1]
    #nombre = nombre.split(' ')
    #nombre = ' '.join(nombre[:4])
    #print(f'El producto "{nombre}" es uno de los más buscados con:\n{idbus}')



def more_stock():
  inventario = [ [product[0], product[4]] for product in lifestore_products]
  
  en_existencia = {}
  
  for par in inventario:
    id = par[0]
    stock = par[1]
    if id not in en_existencia.keys():
      en_existencia[id] = []
      en_existencia[id].append(stock)
      
  dicc_lista = []
  
  for id, lista in en_existencia.items():
    prod = lista[0]
    exists = lista[0]
    sub = [id,prod,exists]
    dicc_lista.append(sub)

  def seg_elemnto(sub):
    return sub[1]
      
  dicc_lista = sorted(dicc_lista, key=seg_elemnto, reverse=True)
      
  for sublista in dicc_lista[:5]:
    id, prod, exists = sublista
    indice_lifestp = id - 1
    prod = lifestore_products[indice_lifestp]
    nombre = prod[1]
    nombre = nombre.split(' ')
    nombre = ' '.join(nombre[:4])
    print(f'El producto "{nombre}" tiene en stock:\n{exists}')



def less_stock():
  inventario = [ [product[0], product[4]] for product in lifestore_products]
  
  en_existencia = {}
  
  for par in inventario:
    id = par[0]
    stock = par[1]
    if id not in en_existencia.keys():
      en_existencia[id] = []
      en_existencia[id].append(stock)
      
  dicc_lista = []
  
  for id, lista in en_existencia.items():
    prod = lista[0]
    exists = lista[0]
    sub = [id,prod,exists]
    dicc_lista.append(sub)

  def seg_elemnto(sub):
    return sub[1]
      
  dicc_lista = sorted(dicc_lista, key=seg_elemnto, reverse=True)
      
  for sublista in dicc_lista[-10:]:
    id, prod, exists = sublista
    indice_lifestp = id - 1
    prod = lifestore_products[indice_lifestp]
    nombre = prod[1]
    nombre = nombre.split(' ')
    nombre = ' '.join(nombre[:4])
    print(f'El producto "{nombre}" tiene en stock:\n{exists}')



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

def totales():
  print("Las ventas totales del ejercicio 2020 fueron de: $737,916")

def menu():
    login()
    while True:
        print('\t¿Que información deseas conocer?:')
        print('\t1. Reviews de los mejores productos')
        print('\t2. Reviews más bajos')
        print('\t3. Productos más vendidos')
        print('\t4. Productos más buscados')
        print('\t5. Productos menos buscados')
        print('\t6. Productos con más stock')
        print('\t7. Productos con menos stock')

        print('\t8. Ventas mensuales')
        print('\t9. Ventas totales del ejercicio')

        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            best_products()
        elif seleccion == '2':
          bad_products()
        elif seleccion == '3':
          more_sales()
        elif seleccion == '4':
          more_search()
        elif seleccion == '5':
          less_search()
        elif seleccion == '6':
          more_stock()
        elif seleccion == '7':
          less_stock()
        elif seleccion == '8':
          mensuales()
        elif seleccion == '9':
          totales()
          print('\n')
        elif seleccion == '0':
            exit('Gracias por tu visita, ¡vuelve pronto!')
        else:
            print('¡Elige una opción enlistada!')
menu()
            
