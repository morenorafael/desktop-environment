from libqtile.config import Key, Group, Key
from libqtile.command import lazy
from settings.keys import mod, keys


groups = [Group(i) for i in [" ", " ", " ", " "]]

for i, group in enumerate(groups):
    current_key = str(i + 1)
    keys.extend([

        # Cambiar al espacio de trabajo N
        Key([mod], current_key, lazy.group[group.name].toscreen()),

        # Enviar ventana al espacio de trabajo N
        Key([mod, "shift"], current_key, lazy.window.togroup(group.name))
    ])
