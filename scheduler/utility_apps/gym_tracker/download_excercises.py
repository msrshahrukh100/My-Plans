
def main():
	import requests
	from bs4 import BeautifulSoup
	from models import Exercise
	base_url = "http://www.total-gym-exercises.com"
	download_url = base_url + "/exercises/index.html"

	print "Making request to ", download_url 
	html = requests.get(download_url).text
	soup = BeautifulSoup(html, 'html.parser')

	final_links = []
	for index, link in enumerate(soup.find_all('a')):
		excercise_link = link.get("href")
		if "#" not in excercise_link and index in range(5, 12):
			print excercise_link
			final_links.append(excercise_link)

	print excercise_link

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
					description=description,
					image_url=image_url)
				print "Saving object", obj.exercise_name
			except Exception as e:
				print "Exception occured : ", e
				continue

