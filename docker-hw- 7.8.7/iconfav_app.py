import requests
import os

url = os.environ.get("SITE_URL")

if url:
    try:
        response = requests.get(f'{url}/favicon.ico')
        if response.status_code == 200:
            with open(f'./img/favicon.ico', 'wb') as icon:
                icon.write(response.content)
                print('Icon downloaded')
    except Exception as e:
        print(f"Error: {e}")
else:
    print("SITE_URL is empty")