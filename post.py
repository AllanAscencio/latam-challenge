import requests

def submit_challenge(name: str, email: str, github_url: str):
    url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"
    payload = {
        "name": name,
        "mail": email,
        "github_url": github_url
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Challenge submitted successfully!")
        else:
            print(f"Failed to submit challenge: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error submitting challenge: {e}")

# Replace with your details
submit_challenge("Allan Ascencio", "allan.ascencio@gmail.com", "https://github.com/AllanAscencio/latam-challenge.git")
