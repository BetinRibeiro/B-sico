cidades = ["Fortaleza","Caucaia","Juazeiro do Norte","Maracanaú","Sobral","Crato","Itapipoca","Maranguape","Iguatu","Quixadá","Canindé","Pacatuba","Quixeramobim","Crateús","Aquiraz","Russas","Aracati","Pacajus","Icó","Tianguá"]

print(cidades)


# ['Fortaleza', 'Caucaia', 'Juazeiro do Norte', 'Maracanaú', 'Sobral', 'Crato', 'Itapipoca', 'Maranguape', 'Iguatu', 'Quixadá', 'Canindé', 'Pacatuba', 'Quixeramobim', 'Crateús', 'Aquiraz', 'Russas', 'Aracati', 'Pacajus', 'Icó', 'Tianguá']

print(*cidades)

# Fortaleza Caucaia Juazeiro do Norte Maracanaú Sobral Crato Itapipoca Maranguape Iguatu Quixadá Canindé Pacatuba Quixeramobim Crateús Aquiraz Russas Aracati Pacajus Icó Tianguá


print(*cidades, sep=" | ")

# Fortaleza | Caucaia | Juazeiro do Norte | Maracanaú | Sobral | Crato | Itapipoca | Maranguape | Iguatu | Quixadá | Canindé | Pacatuba | Quixeramobim | Crateús | Aquiraz | Russas | Aracati | Pacajus | Icó | Tianguá


print(*cidades, sep=" - ", end='\n\n')

print("Finalizou")
