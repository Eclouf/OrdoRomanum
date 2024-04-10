# -*- encoding:utf-8 -*-
from views.GUI.app import TogaApp


"""
    Main class. Responsible for running the application.
    @staticmethod: indicates that the method can be executed without instantiating the class
"""
class Main:
    @staticmethod
    def run():
        try:
            guiApp = TogaApp("Ordo Romanum", "com.eclouf.ordoromanum")
            guiApp.main_loop()
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    Main.run()