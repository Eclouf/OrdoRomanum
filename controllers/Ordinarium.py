# -*- encoding:utf-8 -*-
from controllers.ControllerManager import ControllerManager

"""
    Ordination of the office and mass for the given day.
"""
class Ordination():
    def __init__(self):
        cm = ControllerManager()
        occurence_ctrl = cm.get_occurrence_ctrl()
        competition_ctrl = cm.get_contents_ctrl()
        """
        Morand :
        - Dorénavant, si tu veux importer un controller, fais-le en passant toujours par les fonctions de ControllerManager(), comme je l'ai fait au-dessus
          cela permet d'éviter d'instantier plusieurs fois un controller (donc sauvegarde de mémoire!). Et du coup tu peux instantier autant de fois qu'il le faut
          la class ControllerManager puisqu'il n'a que des méthodes statiques (NB : méthode = fonction d'une classe).
        
        - La logique des controllers doit être exécuté depuis une page (MainPage par exemple car s'est la première qui s'exécute au démarrage), dans le __init__.
          C'est de là que tu peux tester tes fonctions/classes. Tu peux virer le code où je mets 'test colors query' et mettre ton code ici pour tester.
          Bien que je comprenne que tu test en instantiant directement les classes dans leur fichier, mieux vaut le faire en dehors (après tu fait comme tu veux)
          
        Tu peux enlever ce commentaire après si tu veux.
        """
        
    def office(self):
        pass
    
    def mass(self):
        pass