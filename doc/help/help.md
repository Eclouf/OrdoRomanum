# Aide au développement

## Git

Gestionnaire de version, permettant de faciliter la collaboration entre développeur et l'historisation des fichiers.

- `git pull` : permet de récupérer les modifications des branches distantes sur les branches locales (raccourcis pour git fetch (récupérer les commits de la branche distante) puis git merge (applique les commits récupéré de la branche distante))
- `git branch` : liste les branches (git checkout ma_branche si la branche n'a pas été récupéré depuis la branche distante)
- `git branch ma_branche` : crée la branche ma_branche
- `git checkout ma_branche` : basculer vers la branche ma_branche
- `git merge ma_branche` : permet d'appliquer les commits de la branche ma_branche sur la branche sur laquelle je suis actuellement

### Appliquer des modifications

- `git add` : ajoute le fichier modifié (ou créé) à la branche en cours
- `git commit -a -m "My comment"` : valide les modifications sur la branche
- `git push` : transmettre mes commits de ma branche locale vers la branche distante

## Concepts de programmation

- **POO** : Programmation Orientée Objet, principe mettant en oeuvre des classes. Ce sont des entitées composées de variables et de diverses fonctions pour interagir sur ces variables. On parle d'objet lorsqu'on instantie une classe, c'est-à-dire lorsqu'on déclare une classe dans une variable.
- **MVC** : model-vue-controller, le model gère les données persistantes, le controller gère la logique métier (le coeur du projet), et la vue gère l'interaction avec l'utilisateur (GUI par exemple)

## Design patterns

Liste des design patterns les plus connus en Python : <https://refactoring.guru/design-patterns/python>

- **Singleton** : classe qui est instantiée une seule et unique fois lorsque le programme est lancé, même lorsque l'on créé plusieurs objets de cette classe (les deux objets font référence au même objet en RAM)
- **Abstract Factory** : classe permettant de définir des méthodes (méthode=fonction d'une classe) qui devront obligatoirement être définie dans la classe enfant ayant pour parent la classe abstraite
