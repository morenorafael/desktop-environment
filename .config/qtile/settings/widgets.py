from os import path
from libqtile import bar, widget
from libqtile.config import Screen

from settings.path import qtile_path
from themes.material_ocean.colors import colors as ocean
from themes.nordic_darker.colors import colors as nordic


widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=ocean["foreground"],
                    background=ocean["background"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=ocean["foreground"],
                    inactive=ocean["text"],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=ocean["accent"],
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=ocean["background"],
                    other_screen_border=ocean["background"]
                ),
                widget.WindowName(
                    foreground=ocean["accent"],
                    background=ocean["background"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Sep(
                    background=ocean["background"],
                    linewidth=0,
                    padding=5
                ),

                # Wheather
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material_ocean',
                        'images',
                        'bar6.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=ocean["green"],
                    text=" "
                ),
                widget.OpenWeather(
                    foreground=ocean["background"],
                    background=ocean["green"],
                    app_key='ceefe984e6ae8ea8d01560b967bd3a78',
                    cityid='3688689',
                    format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
                    language='es'
                ),
                widget.Sep(
                    background=ocean["green"],
                    linewidth=0,
                    padding=5
                ),

                # UPDATES
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material_ocean',
                        'images',
                        'bar5.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=ocean["yellow"],
                    text=" "
                ),
                widget.CheckUpdates(
                    foreground=ocean["background"],
                    background=ocean["yellow"],
                    colour_have_updates=ocean["background"][0],
                    colour_no_updates=ocean["background"][0],
                    display_format='{updates}',
                    no_update_string='N/A',
                    custom_command='checkupdates',
                    update_interval=1800
                ),
                widget.Sep(
                    background=ocean["yellow"],
                    linewidth=0,
                    padding=5
                ),

                # LAYOUT
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material_ocean',
                        'images',
                        'bar4.png'
                    )
                ),
                widget.CurrentLayoutIcon(
                    foreground=ocean["background"],
                    background=ocean["red"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=ocean["background"],
                    background=ocean["red"],
                ),
                widget.Sep(
                    background=ocean["red"],
                    linewidth=0,
                    padding=5
                ),

                # Systray
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material_ocean',
                        'images',
                        'bar3.png'
                    )
                ),
                widget.Systray(),
                widget.Sep(
                    background=ocean["background"],
                    linewidth=0,
                    padding=5
                ),

                # Keyboard Layout
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material_ocean',
                        'images',
                        'bar2.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=ocean["orange"],
                    text=" "
                ),
                widget.KeyboardLayout(
                    foreground=ocean["background"],
                    background=ocean["orange"],
                    configured_keyboards=["us", "latam"],
                ),
                widget.Sep(
                    background=ocean["orange"],
                    linewidth=0,
                    padding=5
                ),

                # FECHA Y HORA
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material_ocean',
                        'images',
                        'bar1.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=ocean["blue"],
                    text=" "
                ),
                widget.Clock(
                    foreground=ocean["background"],
                    background=ocean["blue"],
                    padding=5,
                    format='%d/%m/%Y - %I:%M %p'
                ),
                # widget.QuickExit(),
            ],
            24,
            background=ocean["background"][0],
            opacity=0.95,
        ),
    ),

    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=ocean["foreground"],
                    background=ocean["background"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=ocean["foreground"],
                    inactive=ocean["text"],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=ocean["accent"],
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=ocean["background"],
                    other_screen_border=ocean["background"]
                ),
                widget.WindowName(
                    foreground=ocean["accent"],
                    background=ocean["background"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Sep(
                    background=ocean["background"],
                    linewidth=0,
                    padding=5
                ),

                # Wheather
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'nordic_darker',
                        'images',
                        'aurora',
                        'nord11-end.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord11"],
                    text=" "
                ),
                widget.OpenWeather(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord11"],
                    app_key='ceefe984e6ae8ea8d01560b967bd3a78',
                    cityid='3688689',
                    format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
                    language='es'
                ),
                widget.Sep(
                    background=nordic["aurora"]["nord11"],
                    linewidth=0,
                    padding=5
                ),

                # UPDATES
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'nordic_darker',
                        'images',
                        'aurora',
                        'nord11-nord12.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord12"],
                    text=" "
                ),
                widget.CheckUpdates(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord12"],
                    colour_have_updates=ocean["background"][0],
                    colour_no_updates=ocean["background"][0],
                    display_format='{updates}',
                    no_update_string='N/A',
                    custom_command='checkupdates',
                    update_interval=1800
                ),
                widget.Sep(
                    background=nordic["aurora"]["nord12"],
                    linewidth=0,
                    padding=5
                ),

                # LAYOUT
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'nordic_darker',
                        'images',
                        'aurora',
                        'nord12-nord13.png'
                    )
                ),
                widget.CurrentLayoutIcon(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord13"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord13"],
                ),
                widget.Sep(
                    background=nordic["aurora"]["nord13"],
                    linewidth=0,
                    padding=5
                ),

                # Keyboard Layout
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'nordic_darker',
                        'images',
                        'aurora',
                        'nord13-nord14.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord14"],
                    text=" "
                ),
                widget.KeyboardLayout(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord14"],
                    configured_keyboards=["us", "latam"],
                ),
                widget.Sep(
                    background=nordic["aurora"]["nord14"],
                    linewidth=0,
                    padding=5
                ),

                # FECHA Y HORA
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'nordic_darker',
                        'images',
                        'aurora',
                        'nord14-nord15.png'
                    )
                ),
                widget.TextBox(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord15"],
                    text=" "
                ),
                widget.Clock(
                    foreground=ocean["background"],
                    background=nordic["aurora"]["nord15"],
                    padding=5,
                    format='%d/%m/%Y - %I:%M %p'
                ),
                # widget.QuickExit(),
            ],
            24,
            background=ocean["background"][0],
            opacity=0.95,
        ),
    ),
]
