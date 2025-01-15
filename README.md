# Bienvenu sur le depot du reseau City Loop by Fewday

> [!CAUTION]
> Ce depot est un **dépôt privé** qui sert a l'éducation et l'apprentissage de l'utilisationn des APIs   **ainsi** que d'exemple de codes sources pour comprendre l'utilisation de ces APIs


> [!NOTE]
> **Ce service est en cours de développement et n'est pas officielle.**

[IDELIS API](https://api.idelis.fr)

[Fewday Studio WS](https://pro.fewday.go.yn.fr/git-ide)


 

> Pour toute question : *support@fewday.go.yn.fr*  

> [!IMPORTANT]
>l'utilisation de l'app GitHub mobile peut altérer l'utilisation se ce dépôt.
>  Merci de signaler tout accès à ce dépôt.
<img src="https://i.ibb.co/6BscpJj/IMG-20240912-WA0002-1.jpg" alt="Logo" width="70">

# Bon développement et amusez-vous bien ! 

### Mise a jour V2.0

---

# 1 Exemple d'utilisation des APIs
## A) Utilisation de l'API Get Stop Monitoring

### Exemple de code HTML et Python utilisé pour Get Stop Monitoring

Exemple avec la ligne **F** *Febus* en direction de *Gare de Pau* avec une arrivée **imminent** et le dernier passage de la ligne dans **42 min**
<img src="https://github.com/FewdayFR/Idelis-data/blob/main/idelis/API/Exemple%20pict/Capture%20d'écran%202025-01-12%20225132.png" border="0">
Même exemple mais le bus est arrivé a quai et est prêt au depart.

<img src="https://github.com/FewdayFR/Idelis-data/blob/main/idelis/API/Exemple%20pict/image_2025-01-14_215054347.png" border="0">

> [!CAUTION]
>  ⚠️Ce message signifie que le bus est peut-être déjà passé / parti 

# 2 Les APIs    **AP'Idelis**
## Bienvenue sur le dépôt d'exemples non officiels de l'API Idelis Pau  

> [!NOTE]
> Ces exemples de code **exclusivement en python** , **ne sont pas officiels** et nécessitent une **clé d'authentification fourni par idelis.**

> [!WARNING]
> Pour l'utilisation de **toutes les API** , la **dépendance request doit etre installée** 
> ```bash  
> pip install -r requirements.txt 
> ```  


## API **AroundMe**  

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
>3. Installer les dépendances nécessaires :
>   ```bash
>   pip install -r requirements.txt   
## API GetStopMonitoring

L'API GetStopMonitoring fournit les informations en temps réel sur les prochains passages de bus à un arrêt spécifique.

### Usage principal
Consulter les horaires des prochains passages pour une ligne ou un arrêt donné.

### Données requises
- Le code Hastus de l'arrêt.
- (Optionnel) : Le nom de la ligne.
- Le nombre de passages souhaités.

### Réponse
Une liste des prochains passages avec les détails suivants :
- Temps d'attente en minutes ou heure exacte d'arrivée,
- Type d'horaire (théorique ou temps réel),
- Indication s'il s'agit du premier ou dernier passage de la journée.
> [!NOTE]
>### Utilisation
>1. Avoir une clé d'authentification et l'URL de l'API.
>2. Installer les dépendances nécessaires :
>   ```bash
>   pip install -r requirements.txt

## API AutoComplete

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
>2. avoir une suite de 3 caractères pour lancer la recherche **Obligatoire** *exemple: BOS -> Bosquet-Pl d'Espagne quai B*
>3. Installer les dépendances nécessaires :
>   ```bash
>   pip install -r requirements.txt
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
>3. Installer les dépendances nécessaires :
>   ```bash
>   pip install -r requirements.txt
 ## Contribuer
Vous pouvez proposer des améliorations ou signaler des problèmes directement sur ce dépôt.

## À propos
Ce dépôt est destiné à aider les développeurs intéressés par l'intégration des données de transport d'Idelis dans leurs applications.

