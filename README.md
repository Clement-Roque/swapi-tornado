# TEST TECHNIQUE : Backend

L'objectif du test est de réaliser une API REST permettant de :
- interroger la base de données (format SQLITE)
- lister un ou tous les personnages de la base avec toutes les informations utiles et les
véhicules et vaisseaux associés
- ajouter, supprimer, mettre à jour un personnage dans la base


# Contenu



Le projet est structuré de la manière suivante :
- Un fichier **Readme**  que vous lisez actuellement, qui introduit le projet, présente son utilisation ainsi que les choix d'implémentation.
-  Un fichier **Pipfile**  qui permet de déclarer les dépendances du projet.
- Un repertoire **project** qui contient l'ensemble des fichiers sources permettant l'execution du projet.
- Un repertoire **test** contenant les fichiers nécessaire à l'execution des tests unitaires du projet.
- Un repertoire **data** contenant la base de données sqlite, fournie pour ce test.

# Lancement du projet

## Pré-requis
Il est nécéssaire d'executer le projet sur une machine disposant de la version **3.7** de Python ainsi que du gestionnaire de dépendances **pipenv**.
Des informations sur **pipenv** et son installation son disponibles à cette adresse :
[https://docs.python-guide.org/dev/virtualenvs/](https://docs.python-guide.org/dev/virtualenvs/)
  
## Mise en place du projet
Une fois le projet cloné, placez vous à sa racine depuis un terminal  et lancez la commande d'installation des dépendances :

`$> pipenv install --dev` pour installer les dépendances de tests et de fonctionnement de de l'API

`$> pipenv install` pour installer uniquement les dépendances de fonctionnement de l'application

## Démarrage de l'API
Pour lancer le serveur API, exécutez la commande suivante dans un terminal depuis la racine du projet :

`$> pipenv run python3 project/app.py`
Le serveur va se mettre en route et sera accessible à l'adresse suivante :
http://localhost:8888/

## Utilisation de l'API

Une fois le serveur démarré, il est possible d'executer les requêtes REST suivantes :

 - **GET** : Récupérer des personnages dans la base
 >Depuis http://localhost:8888/people/ pour récupérer l'ensemble des personnages présents dans la base
 >Depuis http://localhost:8888/people/{id} pour récupérer un personnage en particulier grâce à son id 
 - **POST** : Ajouter un personnage dans la base
 >Depuis http://localhost:8888/people/ et en passant en parametre de la requêtes un personnage au format JSON suivant :
 ```
 {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "birth_year": {"type": "string"},
        "eye_color": {"type": "string"},
        "gender": {"type": "string"},
        "hair_color": {"type": "string"},
        "height": {"type": "string"},
        "mass": {"type": "string"},
        "skin_color": {"type": "string"},
        "homeworld": {"type": "string"},
        "films": {"type": "array"},
        "species": {"type": "array"},
        "starships": {"type": "array"},
        "vehicles": {"type": "array"}
    }
```
 - **PUT** : Mettre à jour un personnage dans la base
 >Depuis http://localhost:8888/people/ et en passant en parametre de la requêtes un personnage au format JSON suivant :
 ```
 {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "birth_year": {"type": "string"},
        "eye_color": {"type": "string"},
        "gender": {"type": "string"},
        "hair_color": {"type": "string"},
        "height": {"type": "string"},
        "mass": {"type": "string"},
        "skin_color": {"type": "string"},
        "homeworld": {"type": "string"},
        "films": {"type": "array"},
        "species": {"type": "array"},
        "starships": {"type": "array"},
        "vehicles": {"type": "array"}
    }
   ```
   - **DELETE** : Supprimer un  personnage dans la base
 >Depuis http://localhost:8888/people/{id} pour supprimer le personnage gràce à son id
 
## Lancement des tests
Pour lancer l'ensemble des tests, exécutez la commande suivante dans un terminal depuis la racine du projet :
`$> pipenv run pytest test/`

**ATTENTION  !** 
Le serveur doit être lancé pour que les tests sur l'API fonctionnent.

# Choix d'implémentation
Dans le cadre de ce projet, j'ai pris les décisions suivantes :

 - J'ai choisi de réaliser ce test en Python et en utilisant le framework web Tornado, connu pour offrir de très bonnes performances dans le cas de connexions simultanées, afin de découvrir et prendre en main ce framework.
 
 - J'ai considèré les id des personnages comme des identifiants fonctionnels et non comme des numéros générés aléatoirement.
 Ils doivent donc conserver une certaine cohérence.
 
 - Dans la base de données fournie initialement, les liens des personnages entre leurs films, espèces, vaisseaux et véhicules sont présents dans des tables de correspondance dédiées (et ce malgré la présence d'un champs spécifique dans la table *People*).
J'ai conservé cette logique dans la conception de mon application.
