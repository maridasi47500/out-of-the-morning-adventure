# network_walk_db.py
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Membre:
    id: str # ton ID de voyage / mac_address
    past_village: str
    current_village: str # ?
    mode: str # wifi / bluetooth / avion / 4G
    music: List[str]

@dataclass
class TrajetPied:
    id: int
    date: datetime
    equipe: List[str] # qui marche avec toi
    gps_start: str
    gps_end: str
    mood: str # côté obscur de la matinée / soleil qui ne te laisse pas dormir
    timestamp_story: str # "one timestamp at a time"

@dataclass
class TrajetTrainBus:
    id: int
    type: str # train / bus
    destination: str # ville où les bateaux/avions arrivent
    qui_guide: str # Qui va vous guider à travers le côté obscur du matin?
    catch_or_miss: str # If it goes right / wrong

@dataclass
class OffreEmploi:
    id: int
    titre: str
    ville: str
    a_postule: bool
    canal: str # email pro uniquement

# Ta BDD principale
class NetworkDB:
    def __init__(self):
        self.membres = []
        self.trajets_pied = []
        self.trajets_transport = []
        self.emplois = []
        self.playlist_groupe = []

    def log_moment(self, texte):
        # "You log the moment, write the story"
        print(f"[{datetime.now()}] {texte} - Would you dare travel from dusk till dawn?")

# Exemple ville
db = NetworkDB()
db.membres.append(Membre("nath_01", "past_village: ville", "deuxieme ville", "bluetooth", ["rock morning"]))
db.trajets_pied.append(TrajetPied(1, datetime.now(), ["toi", "team ville"], "port", "plage", "obscur matin", "on s'est perdus mais on a trouvé"))
db.log_moment("If it goes right: You catch the train. If it goes wrong: You miss the stop. The rain pours.")
