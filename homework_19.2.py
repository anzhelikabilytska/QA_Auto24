import requests
import os

BASE_URL = "http://127.0.0.1:8080"

file_path = "/Users/macos/PycharmProjects/python_test/homework_19.2.py/mars_image_2.jpg"

if not os.path.exists(file_path):
    print(f"Error: The file {file_path} does not exist!")
    exit()

def upload_image(file_path):
    with open(file_path, 'rb') as image:
        files = {'image': image}
        response = requests.post(f"{BASE_URL}/upload", files=files)
        if response.status_code == 201:
            print("Image uploaded successfully!")
            return response.json()["image_url"]
        else:
            print(f"Failed to upload image: {response.json()}")
            return None

def get_image_url(filename):
    headers = {'Content-Type': 'text'}
    response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)
    if response.status_code == 200:
        return response.json()["image_url"]
    else:
        print(f"Failed to get image URL: {response.json()}")
        return None

def delete_image(filename):
    response = requests.delete(f"{BASE_URL}/delete/{filename}")
    if response.status_code == 200:
        print("Image deleted successfully!")
        return True
    else:
        print(f"Failed to delete image: {response.json()}")
        return False

if __name__ == "__main__":
    image_url = upload_image(file_path)
    if not image_url:
        exit()

    filename = image_url.split("/")[-1]

    retrieved_url = get_image_url(filename)
    if retrieved_url:
        print(f"Retrieved Image URL: {retrieved_url}")

    if delete_image(filename):
        print("Image deletion complete.")