# Bienvenu sur le depot Ide'go by Fewday 

> [!CAUTION]
> Ce depot est un **dépôt privé** qui sert a l'éducation et l'apprentissage de l'utilisationn des APIs   **ainsi** que d'exemple de codes pour comprendre l'utilisation de ces APIs


> [!NOTE]
> **Ce dépôt est en cours de développement et n'est pas officielle.**

[IDELIS API](https://api.idelis.fr)

[Fewday Studio WS](https://pro.fewday.go.yn.fr/git-ide)


 

> Pour toute question : *support@fewday.go.yn.fr*  

> [!IMPORTANT]
>l'utilisation de l'app GitHub mobile peut altérer l'utilisation se ce dépôt.
>
>
>  Merci de signaler tout accès à ce dépôt a un administrateur.
<img src="https://i.ibb.co/6BscpJj/IMG-20240912-WA0002-1.jpg" alt="Logo" width="70">

# Bon développement et amusez-vous bien ! 

### Mise a jour V2.5.2

---

# 1 Exemple d'utilisation des APIs
> [!NOTE]
> Ces exemples de code **ne sont pas officiels** et nécessitent une **clé d'authentification fourni par idelis.**



## A) API **AroundMe**  

L'API **AroundMe** retourne les arrêts de bus à proximité d'une localisation donnée.  

### **Usage principal**  
Identifier les arrêts les plus proches en fonction des coordonnées GPS.  

### **Données requises**  
- Latitude et longitude au **format WGS84** (EPSG 4326).  

### **Réponse**  
Une liste d'arrêts avec :  
- leurs coordonnées,  
- leur nom,  
- les lignes desservies,  
- la direction,  
- la distance depuis la position spécifiée.  

### **Exemple d'utilisation**  
Trouver les arrêts situés dans un rayon de quelques mètres autour d'une position GPS (comme celle d'un utilisateur).  
> [!NOTE]
>### Utilisation
>1. Avoir une clé d'authentification et l'URL de l'API.
>2. Avoir accès a certaines options de *l'appareil exemple: Géo-localisation*
  
## B) API GetStopMonitoring

L'API GetStopMonitoring fournit les informations en temps réel sur les prochains passages de bus à un arrêt spécifique.

### Usage principal
Consulter les horaires des prochains passages pour une ligne ou un arrêt donné.

### Données requises
- Le code Hastus de l'arrêt.
- (Optionnel) : Le numéro de la ligne.
- Le nombre de passages souhaités.

### Réponse
Une liste des prochains passages avec les détails suivants :
- Temps d'attente en minutes ou heure exacte d'arrivée,
- Type d'horaire (théorique ou temps réel),
- Indication s'il s'agit du premier ou dernier passage de la journée.
> [!NOTE]
>### Utilisation
>1. Avoir une clé d'authentification et l'URL de l'API.

## C) API AutoComplete

L'API AutoComplete permet de rechercher des arrêts de bus en fonction des premiers caractères de leur nom.

### Usage principal
Récupérer une liste d'arrêts correspondant à une recherche partielle pour aider à la saisie automatique.

### Données requises
- Une chaîne de caractères de 3 lettres minimum pour commencer la recherche.

### Réponse
Une liste des arrêts correspondants avec leurs informations :
- Nom,
- Latitude et longitude,
- Lignes desservies, etc.

### Exemple d'utilisation
Trouver tous les arrêts contenant "Bos" pour potentiellement trouver l'arrêt Bosquet Quai A.
> [!NOTE]
>### Utilisation
>1. Avoir une clé d'authentification et l'URL de l'API.
>2. avoir une suite de 3 caractères pour lancer la recherche **Obligatoire** *exemple: BOS -> Bosquet-Pl d'Espagne*

  ## API Siri

L'API Siri est une interface complète pour accéder aux données en temps réel du réseau de transport d'Idelis. Elle s'appuie sur le protocole SIRI (Service Interface for Real-time Information).

### Usage principal
Accéder à divers types d'informations temps réel, telles que :
- L'état du réseau,
- Les perturbations en cours,
- Les prochains passages aux arrêts.

### Données requises
Dépend des services SIRI spécifiques utilisés (par exemple, StopMonitoring, GeneralMessage, etc.).

### Réponse
Une réponse au format XML ou JSON contenant les informations demandées.

### Exemple d'utilisation
Intégrer des fonctionnalités avancées dans une application pour surveiller les interruptions de service ou les horaires temps réel.
> [!NOTE]
>### Utilisation
>1. Avoir une clé d'authentification et l'URL de l'API.
>2. Avoir accès a certaines options de *l'appareil exemple: Géo-localisation*

 ## Contribuer
Vous pouvez proposer des améliorations ou signaler des problèmes directement sur ce dépôt.

## À propos
Ce dépôt est destiné à aider les développeurs intéressés par l'intégration des données de transport d'Idelis dans leurs applications.

