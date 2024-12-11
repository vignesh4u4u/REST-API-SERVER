import requests
API_URL = "http://184.105.238.154:8080/image_text"
file_paths = [
    r"C:\Users\ASUS\OneDrive\Pictures\invoice-template-us-neat-750px.png",
    r"C:\Users\ASUS\OneDrive\Pictures\billing-templates-free.png",

]
files = [("file", open(file_path, "rb")) for file_path in file_paths]
response = requests.post(API_URL, files=files)
print(response.text)




