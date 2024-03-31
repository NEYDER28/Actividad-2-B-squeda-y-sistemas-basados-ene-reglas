import networkx as nx

#base_conocimiento
R = nx.DiGraph()
R.add_edge("Paradero",	"Virgen poblado", weight= 335)
R.add_edge("Virgen poblado",	"Roberto Velandia", weight= 295)
R.add_edge("Roberto Velandia",	"Entrada Montana", weight= 335)
R.add_edge("Entrada Montana", 	"Empresa Isosceles", weight= 255)
R.add_edge("Empresa Isosceles", 	"Salida Montana", weight= 606)
R.add_edge("Salida Montana",	"Subestacion Enel", weight= 388)
R.add_edge("Subestacion Enel",	"Homecenter", weight= 1965)
R.add_edge("Homecenter",	"Policia Centro", weight= 1228)
R.add_edge("Policia Centro",	"Calle palmeras", weight= 290)
R.add_edge("Calle palmeras",	"Subestación Enel", weight= 1034)
R.add_edge("Virgen poblado",	"Colegio Armonia", weight= 831)
R.add_edge("Colegio Armonia",	"Nuevo Milenio", weight= 852)
R.add_edge("Nuevo Milenio",	"Monumento Gabo", weight= 241)
R.add_edge("Nuevo Milenio",	"Calle 23", weight= 353)
R.add_edge("Calle 23",	"Monumento Gabo", weight= 322)
R.add_edge("Monumento Gabo",	"Entrada Montana", weight= 493)
R.add_edge("Entrada Montana",	"Virgen Santana", weight= 408)
R.add_edge("Virgen Santana",	"Biblioteca", weight= 570)
R.add_edge("Biblioteca",	"Casa de la cultura", weight= 529)
R.add_edge("Casa de la cultura",	"Calle palmeras", weight= 205)

ruta =  str(nx.single_source_dijkstra (R,source="Paradero", target="Homecenter"))

print(ruta)