import requests
from bs4 import BeautifulSoup
from .models import Exercise

base_url = "http://www.total-gym-exercises.com"
download_url = base_url + "/exercises/index.html"


print "Making request to ", download_url 
html = requests.get(download_url).text

soup = BeautifulSoup(html, 'html.parser')

final_links = []
for index, link in enumerate(soup.find_all('a')):
	excercise_link = link.get("href")

	if "#" not in excercise_link and index in range(5, 12):
		final_links.append(excercise_link)

print(final_links)


for link in final_links:
	print("Making request to ", base_url + link)
	html_of_excercise = requests.get(base_url + link).text
	soup_of_excercise = BeautifulSoup(html_of_excercise, 'html.parser')
	muscle_group = link.split("/")[2]
	for index, data in enumerate(soup_of_excercise.find_all('div', attrs={'class':'boxContainerDiv'})):
		try :
			name_of_excercise = data.find('a').text
			description = data.find('ul').text
			image_url = base_url + '/exercises/' + muscle_group + '/' +data.find('img').get('src')
			obj = Exercise.objects.create(
				exercise_name=name_of_excercise,
				muscle_group=muscle_group,
				image_url=image_url)
			break
		except :
			continue

		# if index in range(16, 27):
		# 	# print(dir(link))
		# 	print(link.next_element)
		# 	print(index, link.text)
	break
