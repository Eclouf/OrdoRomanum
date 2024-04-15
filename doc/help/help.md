# Aide au développement

## Git

Gestionnaire de version, permettant de faciliter la collaboration entre développeur et l'historisation des fichiers.

- `git pull` : permet de récupérer les modifications des branches distantes sur les branches locales (raccourcis pour git fetch (récupérer les commits de la branche distante) puis git merge (applique les commits récupéré de la branche distante))
- `git branch` : liste les branches (git checkout ma_branche si la branche n'a pas été récupéré depuis la branche distante)
- `git branch ma_branche` : crée la branche ma_branche
- `git checkout ma_branche` : basculer vers la branche ma_branche
- `git merge ma_branche` : permet d'appliquer les commits de la branche ma_branche sur la branche sur laquelle je suis actuellement
- `git stash` : permet de mettre de côté les modifications (avant commit), par exemple si on se trompe de branche et que l'on veut déplacer les modifications vers la bonne branche
- `git stash pop` : permet de ramener les dernières modifications mises de côté sur la branche actuelle
- `git log` : afficher les listes des derniers commit de la branche actuelle (appuyer sur `q` pour quitter la vue des logs)

### Appliquer des modifications

- `git add` : ajoute le fichier modifié (ou créé) à la branche en cours
- `git commit -a -m "My comment"` : valide les modifications sur la branche
- `git commit --amend` : valider les modifications en les ajoutant au dernier commit (si par exemple on oublie de valider des modifications alors qu'on vient de créer un commit. Cela évite la création d'un nouveau commit avec un même message que le précédent commit)
- `git push` : transmettre mes commits de ma branche locale vers la branche distante

### Résoudre une erreur de pull ou push

<https://docs.github.com/fr/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line>

L'erreur la plus fréquente est d'avoir la branche distante et la branche locale qui divergent à cause d'un ou plusieurs commits de la branche distante qui ne sont pas présent avant le dernier commit de la branche locale (si quelqu'un a envoyé ses modifications sur la branche distante et qu'une autre personne travaillant sur la même branche en locale a commiter ses modifications sans récupérer auparavant les modifications de l'autre personne). Pour résoudre ce problème, il faut faire un "rebase", c'est-à-dire appliquer les commits de la branche distante avant les derniers qui sont sur la branche locale et réappliquer les dernires commits de la branche locale : `git pull --rebase`
S'il y a écrit `CONFLICT` après le "rebase", c'est qu'un commit de la branche distante fait état d'une modification sur un fichier qui est aussi modifier par un commit de la branche locale.
Dans le fichier concerné, on trouvera ce genre de notation pour la ligne où la modification  :

```txt
< < < < < HEAD (ligne de la branche distante)
Je m'appelle John Connan
=======
Je m'appelle John et lui c'est Toto
> > > > > new_branch_to_merge_later (ligne de la branche locale)
```

Ici on veut garder les modifications de la branche distante et locale. On supprime donc ce qui entre les `<<< ... === ... >>>` en gardant ou modificant ce que l'on veut.
Par exemple, on veut les deux modifications. On écrit et sauvegarde le fichier avec :

```txt
Je m'appelle John Connan et lui c'est Toto
```

On ajoute les modifications, on commit et on envoie sur la branche distante : `git add .`, `git commit -a -m "Fix conflicts"`, `git push`.

## Concepts de programmation

- **POO** : Programmation Orientée Objet, principe mettant en oeuvre des classes. Ce sont des entitées composées de variables et de diverses fonctions pour interagir sur ces variables. On parle d'objet lorsqu'on instantie une classe, c'est-à-dire lorsqu'on déclare une classe dans une variable <https://www.pythoncheatsheet.org/cheatsheet/oop-basics>
- **MVC** : model-vue-controller, le model gère les données persistantes, le controller gère la logique métier (le coeur du projet), et la vue gère l'interaction avec l'utilisateur (GUI par exemple)
- **principe KISS** : Acronyme pour "Keep It Stupid Simple" ou "Ne complique pas les choses". L'idée est d'éviter d'ajouter inutilement de la complexité autant que possible. Personnellement, je préconise de concevoir les choses simplement, en maîtrisant le code déjà écrit. Lorsqu'on identifie un moyen de résoudre un problème, notamment dans la *répétition inutile de code* et *les fichiers/fonctions à 1000 lignes de code incompréhensibles parce que le cerveau explose*, on applique et on itère ainsi de suite. (création de classe abstraite, héritage, séparation du code en plusieurs fonctions, en controller, etc.). Dans la structure que j'ai faite, rien n'est figé et est sujet à changement.

## Design patterns

Liste des design patterns les plus connus en Python : <https://refactoring.guru/design-patterns/python>

- **Singleton** : classe qui est instantiée une seule et unique fois lorsque le programme est lancé, même lorsque l'on créé plusieurs objets de cette classe (les deux objets font référence au même objet en RAM)
- **Abstract Factory** : classe permettant de définir des méthodes (méthode=fonction d'une classe) qui devront obligatoirement être définie dans la classe enfant ayant pour parent la classe abstraite

## Cheatsheet Python

Aide-mémoire pour le langage Python, une documentation concise expliquant les principaux concepts sur Python : <https://www.pythoncheatsheet.org/>

## Logiciels tiers

- [**GitAhead**](https://gitahead.github.io/gitahead.com/) : un client Git qui peut aider visuellement à mieux comprendre le fonctionnement.
- [**DBeaver**](https://dbeaver.io/) : un logiciel d'administration de base de donnée relationnelle SQL.
