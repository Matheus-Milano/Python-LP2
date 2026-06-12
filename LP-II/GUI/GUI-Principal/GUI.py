#!/usr/bin/env python
# -*- coding: utf-8 -*

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:

    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Minha Janela")
        janela.set_border_width(20)
        janela.set_default_size(1000, 800)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
   prog = Aplicacao()
   Gtk.main()