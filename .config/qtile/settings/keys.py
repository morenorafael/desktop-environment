from libqtile.config import Key
from libqtile.lazy import lazy


mod = "mod4"
terminal = "alacritty"

keys = [

    # VENTANAS

    # Cambiar entre ventanas
    Key([mod], "Left", lazy.layout.left(),
        desc="Mover el enfoque a la izquierda"),
    Key([mod], "Right", lazy.layout.right(),
        desc="Mover el enfoque a la derecha"),
    Key([mod], "Down", lazy.layout.down(),
        desc="Mover el enfoque hacia abajo"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Mover el enfoque hacia arriba"),
    # Key([mod], "space", lazy.layout.next(),
    #    desc="Mover el foco de la ventana a otra ventana"),

    # Mueve las ventanas entre las columnas izquierda/derecha osube/baja en la
    # pila actual.
    # Si se sale del rango en el diseño de Columnas, se creará una nueva
    # columna.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Mover ventana hacia arriba"),

    # Haga crecer las ventanas. Si la ventana actual está en el borde de la
    # pantalla y la dirección será hacia el borde de la pantalla, la ventana
    # se encogerá.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Hacer crecer la ventana a la izquierda"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Hacer crecer la ventana a la derecha"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Hacer crecer la ventana hacia abajo"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(),
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

    # SCREENSHOT
    Key([mod], "s",
        lazy.spawn("scrot ~/screenshots/%Y-%m-%d-%T-screenshot.png"),
        desc="Captura de pantalla"),

    # ------------ Hardware Configs ------------

    # Volume
    Key([mod], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([mod], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([mod], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([mod], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
