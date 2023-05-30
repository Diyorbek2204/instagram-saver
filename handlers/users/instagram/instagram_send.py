import requests
import json


def instagram_download(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "408e55bb6amsh41a8f40824ce0bep16c762jsn9a9cc883dbc6",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	rest = json.loads(response.text)
	if 'error' in rest:
		return 'Error happened!'
	else:
		dict = {}
		if rest['Type'] == "Post-Image":
			dict['type'] = 'image'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == "Post-Video":
			dict['type'] = 'video'
			dict['media'] = rest['media']
			return dict
		elif rest['Type'] == 'Carousel':
			dict['type'] = 'carousel'
			dict['media'] = rest['media']
			return dict
		else:
			return 'Bad'