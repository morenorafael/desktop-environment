from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys


groups = [Group(i) for i in [" ", " ", " ", " "]]

for i, group in enumerate(groups):
    current_key = str(i + 1)
    keys.extend([

        # Switch to workspace N
        Key([mod], current_key, lazy.group[group.name].toscreen()),

        # Send window to workspace N
        Key([mod, "shift"], current_key, lazy.window.togroup(group.name))
    ])
