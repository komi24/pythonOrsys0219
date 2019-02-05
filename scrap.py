import requests
from bs4 import BeautifulSoup
from time import sleep

for i in range(4):
	page = requests.get("http://www.ffbb.com/jouer/trouver-un-club?page=%d&DepartementClub=91"%(i+1))

	parsed_page = BeautifulSoup(page.content, 'html.parser')

	clubs = parsed_page.select("span.salle-title")
	print(len(clubs))
	print([club.text for club in clubs])

	tels = parsed_page.select("span.tel-val")

	print(list(zip([tel.text for tel in tels],[club.text for club in clubs])))

	sleep(2)