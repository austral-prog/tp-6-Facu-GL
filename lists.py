def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements
    length = len(lista)
    if length > 5:
        del lista[5]
        del lista[4]
        del lista[0]
    elif length == 5:
        del lista[4]
        del lista[0]
    elif 0 < length <= 5:
        del lista[0]
    elif length == 0:
        print([])
    return lista


def add_elements(list_to_add_elements):
    agregar = list_to_add_elements
    agregar.insert(0, "Pink")
    agregar.append("Yellow")
    return agregar


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        valor = True
    else:
        valor = False
    return valor


def check_lists(list_to_compare1, list_to_compare2):
    lista1 = list_to_compare1
    lista2 = list_to_compare2
    if len(lista1) >= 3 and len(lista2) >= 3:
        if lista1[2] == lista2[2]:
          Valor = True
        else:
          Valor = False
    else:
        Valor = False
    return Valor


def list_of_lists(list_of_lists_to_modify):
    sub1 = list_of_lists_to_modify[0]
    sub2 = list_of_lists_to_modify[1]
    sub3 = list_of_lists_to_modify[2]
    if len(sub1) > 0:
        sub1 = sub1[0:2]
    else:
        sub1 = []
    if len(sub2) >= 2:
        sub2 = sub2[1:4]
    else:
        sub2 = []
    if len(sub3) > 0:
        sub3 = sub3[-2:]
    todo = [sub1, sub2, sub3]
    return todo
