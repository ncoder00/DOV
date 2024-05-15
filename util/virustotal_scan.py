# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv('api_keys.env')
# virustotal_api_key = os.getenv('VIRUSTOTAL_API_KEY')

# def get_virustotal_scan(url):
#     """Check URL for malware and phishing using VirusTotal."""
#     headers = {'x-apikey': virustotal_api_key}
#     params = {'url': url, 'apikey': virustotal_api_key}
#     response = requests.post('https://www.virustotal.com/api/v3/urls', data=params, headers=headers)
#     report_url = response.json()["data"]["links"]["self"]
#     report_response = requests.get(report_url, headers=headers)
#     return report_response.json()["data"]["attributes"]
