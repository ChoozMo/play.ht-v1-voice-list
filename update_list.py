import requests

if __name__ == "__main__":
    url = "https://api.play.ht/api/v1/getVoices"

    headers = {
        "accept": "application/json",
        "AUTHORIZATION": "7a78348efac7468b8188c090a24a0559",
        "X-USER-ID": "HEQLQR1WgpYtN0SEyKoWBsLiZXX2"
    }

    response = requests.get(url, headers=headers)

    with open('list.json', 'w') as f:
        f.write(response.text)