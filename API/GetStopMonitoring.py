import requests

# Clé API IDELIS
API_KEY = "your API KEY"

# URL de l'API GetStopMonitoring
URL_GET_STOP_MONITORING = "Votre URL de l'api"

# Headers de la requête
HEADERS = {
    "X-AUTH-TOKEN": API_KEY,
    "Content-Type": "application/json"
}

def get_stop_monitoring(stop_code, line=None, next_passages=3):
    # Voir les paramètres ligne 35 <> 37
    
    # Corps de la requête
    body = {
        "code": stop_code,
        "next": next_passages
    }
    if line:
        body["ligne"] = line

    # Requête HTTP GET
    response = requests.get(URL_GET_STOP_MONITORING, headers=HEADERS, json=body)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return None

# Exemple d'utilisation
if __name__ == "__main__":
    stop_code = "F-EBOS_A"  # Remplacez par le code Hastus de votre arrêt
    line = None             # Optionnel : spécifiez une ligne si nécessaire
    next_passages = 3       # Nombre de passages à afficher

    stop_data = get_stop_monitoring(stop_code, line, next_passages)
    if stop_data:
        print("Prochains passages :", stop_data)
