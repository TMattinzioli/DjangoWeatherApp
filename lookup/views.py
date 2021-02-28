#This is my views.py file :D

from django.shortcuts import render

# Create home HTML here. When you want to enter webpage, you send a "request".
def home(request):
	#This is our view.
	import json
	import requests

	if request.method == "POST":
		#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=47DCB454-DD6C-4931-9AE0-F71E71BD9F88
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=47DCB454-DD6C-4931-9AE0-F71E71BD9F88")

		try:
			api = json.loads(api_request.content)
		except	Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "Good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "Moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung cancer disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of paricles in the air."
			category_color = "UnhealthyforSensitiveGroups"	  

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "VeryUnhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "Hazardous"	
			


		#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=47DCB454-DD6C-4931-9AE0-F71E71BD9F88
		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description, 
			'category_color': category_color
			})


	else:	
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=47DCB454-DD6C-4931-9AE0-F71E71BD9F88")

		try:
			api = json.loads(api_request.content)
		except	Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "Good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "Moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung cancer disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of paricles in the air."
			category_color = "UnhealthyforSensitiveGroups"	  

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			category_color = "VeryUnhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "Hazardous"	
			


		#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=47DCB454-DD6C-4931-9AE0-F71E71BD9F88
		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description, 
			'category_color': category_color
			})

def about(request):
	#This is our view.
	return render(request, 'about.html', {})	