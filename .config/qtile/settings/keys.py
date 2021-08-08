from libqtile.config import Key
from libqtile.lazy import lazy


mod = "mod4"
terminal = "alacritty"

keys = [

    # VENTANAS

    # Cambiar entre ventanas
    Key([mod], "h", lazy.layout.left(),
        desc="Mover el enfoque a la izquierda"),
    Key([mod], "l", lazy.layout.right(),
        desc="Mover el enfoque a la derecha"),
    Key([mod], "j", lazy.layout.down(),
        desc="Mover el enfoque hacia abajo"),
    Key([mod], "k", lazy.layout.up(),
        desc="Mover el enfoque hacia arriba"),
    # Key([mod], "space", lazy.layout.next(),
    #    desc="Mover el foco de la ventana a otra ventana"),

    # Mueve las ventanas entre las columnas izquierda/derecha osube/baja en la
    # pila actual.
    # Si se sale del rango en el diseño de Columnas, se creará una nueva
    # columna.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Mover ventana hacia arriba"),

    # Haga crecer las ventanas. Si la ventana actual está en el borde de la
    # pantalla y la dirección será hacia el borde de la pantalla, la ventana
    # se encogerá.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Hacer crecer la ventana a la izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Hacer crecer la ventana a la derecha"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Hacer crecer la ventana hacia abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Hacer crecer la ventana hacia arriba"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Restablecer todos los tamaños de ventana"),

    # Alternar entre lados divididos y no divididos de la pila.
    # Split = se muestran todas las ventanas
    # Unsplit = 1 ventana mostrada, como el diseño Max, pero aún con múltiples
    # paneles de pila
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #    desc="Alternar entre lados divididos y no divididos de la pila"),
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Lanzar terminal"),

    # Alternar entre diferentes diseños como se define a continuación
    Key([mod], "Tab", lazy.next_layout(),
        desc="Alternar entre layouts"),
    Key([mod], "w", lazy.window.kill(),
        desc="Mata ventana enfocada"),

    Key([mod, "control"], "r", lazy.restart(),
        desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(),
    #    desc="Genere un comando usando un widget de solicitud"),

    # PROGRAMAS
    # MENU
    Key([mod], "m", lazy.spawn("rofi -show drun"),
        desc="Lanzar Rofi"),
    Key([mod], "e", lazy.spawn("thunar"),
        desc="Lanzar Thunar"),

    # NAVEGACION DE VENTANAS
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"),
        desc="Lanzar Rofi Nav"),
]
