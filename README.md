# Bienvenu sur le dépôt d'exemple non officiel de l'API d'Idelis Pau
> [!NOTE]
> Ces exemples de code python ne sont pas officiels et nécessitent une clef d'authentification fourni par idelis.

> [!WARNING]
> Pour l'utilisation de **toutes les API** , la **dépendance request doit etre installée**
>
>  ``pip install requests``

Bon développement et amusez vous bien !

> *questions -> support@pro.fewday-studio.go.yn.fr*

## API AroundMe

**L'API AroundMe** retourne les arrêts de bus à proximité d'une localisation donnée.

**Usage principal :** Identifier les arrêts les plus proches en fonction des coordonnées GPS.

**Données requises :** Latitude et longitude au **format WGS84** (EPSG 4326).


**Réponse :** Une liste d'arrêts avec leurs coordonnées, leur nom, les lignes desservies, la direction, et la distance depuis la position spécifiée.

**Exemple d'utilisation :** Trouver les arrêts dans un rayon de quelques mètres autour d'une position GPS (comme celle d'un utilisateur).

 
>utilisation :
>
>Avoir une clef d'authentification et l'url de l'API
>
>installer les dépendances
>
>``pip install requests geopy``
>

## API GetStopMonitoring

**L'API GetStopMonitoring** fournit les informations en temps réel des prochains passages de bus à un arrêt spécifique.

**Usage principal :** Consulter les horaires des prochains passages pour une ligne ou un arrêt donné.

**Données requises :**


Le code Hastus de l'arrêt.

*Optionnel : Le nom de la ligne.*

Le nombre de passages souhaités.


**Réponse :** Une liste des prochains passages avec les détails suivants :

Temps d'attente en minutes ou heure exacte d'arrivée.

Type d'horaire (théorique ou temps réel).

Indication s'il s'agit du premier ou dernier passage de la journée.

>utilisation :
>
>Avoir une clef d'authentification et l'url de l'API
>
>installer les dépendances
>
>``pip install requests``
>


## API AutoComplete 

L'API AutoComplete permet de rechercher des arrêts de bus en fonction des premiers caractères de leur nom.

**Usage principal**: Récupérer une liste d'arrêts correspondant à une recherche partielle pour aider à la saisie automatique.

**Données requises :**

Une chaîne de caractères de **3 lettres minimum** pour commencer la recherche.


**Réponse :** Une liste des arrêts correspondants avec leurs informations (nom, latitude, longitude, lignes desservies, etc.).

Exemple d'utilisation : Trouver tous les arrêts contenant "Bos" pour potentiellement trouver l'arret bosquet quai A.
>utilisation :
>
>Avoir une clef d'authentification et l'url de l'API
>
>installer les dépendances
>
>``pip install requests``


### Contribuer :  

Vous pouvez proposer des améliorations ou signaler des problèmes directement sur ce dépôt.  

---

### À propos :  

Ce dépôt est destiné à aider les développeurs intéressés par l'intégration des données de transport d'Idelis dans leurs applications.
