import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class AplicacaoTeste:
    def __init__(self):
        tela = Gtk.Window()
        tela.set_title("sla")
        tela.set_default_size(400, 200)
        rotulo = Gtk.Label()
        rotulo.set_label("MATHEUS HENRIQUE MILANO\n 2° Informática")
        tela.add(rotulo)
        rotulo.show()
        tela.show()

if __name__ == '__main__':
    janela = AplicacaoTeste()
    Gtk.main()