import requests
url = "http://184.105.238.154:8080/generate"
form_data = {
    "input_prompt": "what about the AIDS, please give the full details.."
}
try:
    response = requests.post(url, data=form_data)
    if response.status_code == 200:
        json_response = response.json()
        generated_text = json_response.get("generated_text", "")
        print(generated_text)
    else:
        print(f"Failed to get response. HTTP Status Code: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")






