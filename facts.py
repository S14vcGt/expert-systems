# facts.py
from experta import Fact, Field

class Organism(Fact):
    """Información sobre el organismo."""
    nivel_organizacion = Field(str, mandatory=True)
    simetria = Field(str, mandatory=True)
    capas_germinales = Field(str, mandatory=True)
    cavidad_corporal = Field(str, mandatory=True)
    segmentacion = Field(str, mandatory=True)
    sistema_digestivo = Field(str, mandatory=True)
    sistema_nervioso = Field(str, mandatory=True)
    sistema_corporal = Field(str, mandatory=True)
    reproduccion = Field(str, mandatory=True)
    habitat = Field(str, mandatory=True)
