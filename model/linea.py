from dataclasses import dataclass

@dataclass
class Linea:
    id_linea: int
    nome: str
    velocita: float
    intervallo: float
    colore: str

    def __str__(self):
        return f"{self.id_linea}"

    def __hash__(self):
        hash(self.id_linea)