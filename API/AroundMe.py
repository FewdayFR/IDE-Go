import requests
from geopy.geocoders import Nominatim

def get_device_location():
    """Obtenir la localisation de l'appareil via IP."""
    try:
        # Utiliser le service de géolocalisation de geopy
        geolocator = Nominatim(user_agent="device_locator")
        location = geolocator.geocode("me", timeout=10)  # "me" pour la localisation basée sur IP
        
        if location:
            print(f"Localisation obtenue : {location.latitude}, {location.longitude}")
            return location.latitude, location.longitude
        else:
            print("Impossible d'obtenir la localisation.")
            return None, None
    except Exception as e:
        print(f"Erreur lors de la récupération de la localisation : {e}")
        return None, None

def call_around_me_api(latitude, longitude, api_url, api_key):
    """Appeler l'API AroundMe avec les coordonnées fournies."""
    if latitude is None or longitude is None:
        print("Coordonnées non disponibles. Impossible de faire la requête.")
        return

    headers = {
        "X-AUTH-TOKEN": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "latitude": latitude,
        "longitude": longitude
    }

    try:
        response = requests.get(api_url, headers=headers, params=payload)
        if response.status_code == 200:
            print("Réponse de l'API AroundMe :")
            print(response.json())
        else:
            print(f"Erreur : {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Une erreur est survenue lors de l'appel API : {e}")

# URL et clé API
API_URL = "VOTRE_URL_API"  # Remplacez par l'URL de l'API AroundMe
API_KEY = "VOTRE_CLE_API"  # Remplacez par votre clé API

# Récupérer la localisation de l'appareil
latitude, longitude = get_device_location()

# Appeler l'API AroundMe
call_around_me_api(latitude, longitude, API_URL, API_KEY)
