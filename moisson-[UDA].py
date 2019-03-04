#coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "uda.csv"
# J'ai voulu répertorier tous les "utilisateurs" de l'UDA (membres,stagiaires,etc.)...
#...et en retirer quelques informations utiles pour les retrouver facilement.

# Après plusieurs essais, l'URL du bottin était la plus facile à manipuler...
#...étant donné que le numéro associé à chaque utiilsateur est un numéro aléatoire à 6 chiffres. 
a = "http://uda.ca/bottin?page=" 


entetes = {
	"User-Agent": "Laurent Corbeil",
	"From": "514-827-3723"
}
l1 = range(0,574)# les 575 pages du bottin
for numero in l1:
	
	url = a + str(numero)

	contenu = requests.get(url,headers=entetes)

	page = BeautifulSoup(contenu.text,"html.parser")

	#print()
	nom = page.find("h3").text #isole le nom
	#print(nom)
	statut = page.find("h4").text #isole l'information complémentaire(membres,stagiaires,etc.)
	#print (statut)
	home = "http://uda.ca/"
	adresse = home + (page.find(class_="artist-link")["href"])
	# l'addition de la variable "home" avec "utilisateurs/******" pour avoir l'URL de chaque utilisateur.
	infos = [nom,statut,adresse]
	print(infos)
	print("~"*80)
	
	#PROBLÈME MAJEUR DANS MON MOISSONNAGE:
	# J'étais incapable d'ajouter un {find_all} et de considérer uniquement le texte {.text}...
	#...sur la même variable. 

	#Ce qui fait en sorte que j'ai PRINT uniquement les infos du premier utilisateur de chaque page, soit 575. :(

	f2 = open(fichier, "a")
	uda = csv.writer(f2)
	uda.writerow(infos)




	
