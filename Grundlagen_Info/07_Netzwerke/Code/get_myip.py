import requests

def get_my_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        response.raise_for_status()
        ip = response.json().get('ip')
        print(f"My public IP address is: {ip}")
    except requests.RequestException as e:
        print(f"Error retrieving IP address: {e}")

if __name__ == "__main__":
    get_my_ip()