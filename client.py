from grafo import Grafo

# Se crea un nuevo grafo con un ID
grafo_1 = Grafo('1')

# Se llama al metodo exportar con el tipo que se quiere
response = grafo_1.exportar('XML')

# Se imprime la respuesta
print(response)

# Se llama al metodo exportar con un tipo que aún no está implementado
response = grafo_1.exportar('PDF')

# Se imprime la respuesta
print(response)