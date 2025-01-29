from experta import KnowledgeEngine, Rule
from facts import Organism
from phyla_data import phyla_caracteristicas


class PhylumExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.phylum_coincidencias = {phylum: 0 for phylum in phyla_caracteristicas}
        self.total_caracteristicas = len(next(iter(phyla_caracteristicas.values())))

    def verificar_coincidencias(self, organism, phylum, caracteristicas):
        coincidencias = sum(
            1 for key, value in caracteristicas.items() if organism.get(key) == value
        )
        self.phylum_coincidencias[phylum] = coincidencias

    @Rule(Organism())
    def evaluar_phyla(self):
        organism = self.facts[1]
        for phylum, caracteristicas in phyla_caracteristicas.items():
            self.verificar_coincidencias(organism, phylum, caracteristicas)
        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("\nResultados:")

        # Ordenamos los phyla por porcentaje de coincidencias, de mayor a menor
        phyla_ordenados = sorted(
            self.phylum_coincidencias.items(),
            key=lambda item: (item[1] / self.total_caracteristicas) * 100,
            reverse=True
        )

        # Calculamos el porcentaje de coincidencias para cada phylum
        phylum_porcentajes = {
            phylum: (coincidencias / self.total_caracteristicas) * 100
            for phylum, coincidencias in phyla_ordenados
        }

        # Encontramos el phylum más probable (el primero en la lista)
        phylum_mas_probable = phyla_ordenados[0]
        porcentaje_mas_probable = phylum_porcentajes[phylum_mas_probable[0]]
        print(f"El phylum más probable es: {phylum_mas_probable[0]} con {phylum_mas_probable[1]}/{self.total_caracteristicas} coincidencias ({porcentaje_mas_probable:.2f}%)\n")

        # Mostramos los demás phyla entre 70% y 100%
        print("Otros posibles phyla:")
        contador = 0    # Cuenta las coincidencias
        for phylum, porcentaje in phylum_porcentajes.items():
            if 70 <= porcentaje < 100:
                coincidencias = self.phylum_coincidencias[phylum]
                contador += 1
                print(f"{phylum} con {coincidencias}/{self.total_caracteristicas} coincidencias ({porcentaje:.2f}%)")
            
        if contador == 0:
            print("No hay otros posibles phyla.")



