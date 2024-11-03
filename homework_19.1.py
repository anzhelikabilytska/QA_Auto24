import requests

api_endpoint = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
query_params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    photos_data = response.json().get('photos', [])

    if photos_data:
        for index, item in enumerate(photos_data[:2], start=1):
            image_url = item.get('img_src')
            print(f"Fetching photo {index} from {image_url}")

            image_data = requests.get(image_url)
            if image_data.status_code == 200:
                with open(f"mars_image_{index}.jpg", "wb") as file:
                    file.write(image_data.content)
                print(f"Photo saved as mars_image_{index}.jpg")
            else:
                print(f"Error downloading photo {index}")
    else:
        print("No photos found for the specified query.")
else:
    print("Error: Could not retrieve data from NASA API.")