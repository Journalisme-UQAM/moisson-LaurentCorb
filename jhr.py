#coding: utf-8

### Excellente idée de script!
### Très bonne documentation, même de ce qui n'a pas bien fonctionné.
### Tu étais proche...

import csv
import requests
from bs4 import BeautifulSoup

fichier = "uda_jhr.csv" ### Je renomme ton fichier
fichier2 = "uda2_jhr.csv" ### J'en crée un autre pour enregistrer les infos de la solution que j'ai pour toi.

# J'ai voulu répertorier tous les "utilisateurs" de l'UDA (membres,stagiaires,etc.)...
#...et en retirer quelques informations utiles pour les retrouver facilement.

# Après plusieurs essais, l'URL du bottin était la plus facile à manipuler...
#...étant donné que le numéro associé à chaque utiilsateur est un numéro aléatoire à 6 chiffres. 
a = "http://uda.ca/bottin?page=" 


entetes = {
	"User-Agent": "Laurent Corbeil",
	"From": "514-827-3723"
}

l1 = range(0,574)# les 575 pages du bottin ### OUPS -> ici, il te manque les 2 dernières pages, car ta boucle arrête à la p. 573
# l1 = range(574,576) ### J'ai complété les deux dernières pages du bottin
for numero in l1:
	
	url = a + str(numero)

	contenu = requests.get(url,headers=entetes)

	page = BeautifulSoup(contenu.text,"html.parser")

	#print()
	# nom = page.find("h3").text #isole le nom
### Comme je l'expliquais dans ma vidéo, un simple «.find» ne retourne que le premier élément correspondant dans une page

	#print(nom)
	# statut = page.find("h4").text #isole l'information complémentaire(membres,stagiaires,etc.)
	#print (statut)
	# home = "http://uda.ca/"
	# adresse = home + (page.find(class_="artist-link")["href"])
	# l'addition de la variable "home" avec "utilisateurs/******" pour avoir l'URL de chaque utilisateur.
	# infos = [nom,statut,adresse]
	# print(infos)
	# print("~"*80)
	
	#PROBLÈME MAJEUR DANS MON MOISSONNAGE:
	# J'étais incapable d'ajouter un {find_all} et de considérer uniquement le texte {.text}...
	#...sur la même variable. 

	#Ce qui fait en sorte que j'ai PRINT uniquement les infos du premier utilisateur de chaque page, soit 575. :(

	# f2 = open(fichier, "a")
	# uda = csv.writer(f2)
	# uda.writerow(infos)


### La solution, ici, pourrait ressembler à ceci:

	artistes = page.find("div", class_="view-content").find_all("li")
	for artiste in artistes:
		nom = artiste.find("h3").text
		statut = artiste.find("h4").text
		adresse = "http://uda.ca/{}".format(artiste.find("a",class_="artist-link")["href"])

		info = [nom,statut,adresse]
		print(numero,info)

		pascale = open(fichier2, "a")
		bussieres = csv.writer(pascale)
		bussieres.writerow(info)

### Mais ce ne serait pas tout.
### Il faudrait qu'à chaque page d'artiste, ton script aille aussi recueillir les informations de chaque artiste: agence, formation (pour voir combien de membres de l'UDA ont une formation en journalisme, par exemple!), etc.
