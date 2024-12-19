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
cette api récupère les arrêts a proximité d'une certaine localisation 
>utilisation :
>
>Avoir une clef d'authentification et l'url de l'API
>
>installer les dépendances
>
>``pip install requests geopy``
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
