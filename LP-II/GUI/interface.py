import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Tela:
    """Classe que representa a interface gráfica"""

    def __init__(self):
        """Construtor para instanciar a Tela"""
        janela = Gtk.Window()
        janela.show()

if __name__ == '__main__':
    """
       Verificar origem da execução e só rodar
       quando for o próprio arquivo executado
    """
    instanciaDeTela = Tela()
    Gtk.main()