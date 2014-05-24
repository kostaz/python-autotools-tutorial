from gi.repository import Gtk

class Application(object):
    def __init__(self, *args, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        self._create_main_window()

    def _create_main_window(self):
        self.window = Gtk.Window()
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_title("%s v%s" % (self.package, self.version))
        self.window.set_default_size(300, 150)
        self.window.set_border_width(20)
        self.window.add(Gtk.Label("Hello world!"))

    def run(self):
        self.window.show_all()
        Gtk.main()

