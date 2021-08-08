# from typing import List  # noqa: F401

from libqtile import hook

from os import path
import subprocess

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults, screens
from settings.mouse import mouse


@hook.subscribe.startup_once
def autostart():
    subprocess.call([
        path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')
    ])


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wmname = "LG3D"
