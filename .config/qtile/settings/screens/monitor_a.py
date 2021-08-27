from os import path
from libqtile import bar, widget
from libqtile.config import Screen

from settings.path import qtile_path
from themes.material.oceanic.colors import colors as ocean


screen = Screen(
    top=bar.Bar(
        [
            widget.GroupBox(
                foreground=ocean["foreground"],
                background=ocean["background"],
                font='UbuntuMono Nerd Font',
                fontsize=19,
                margin_y=3,
                margin_x=0,
                padding_y=30,
                padding_x=15,
                borderwidth=2,
                active=ocean["foreground"],
                inactive=ocean["foreground"],
                rounded=False,
                highlight_method='line',
                highlight_color=ocean["background"],
                this_current_screen_border=ocean["accent"],
                this_screen_border=["#5c5c5c", "#5c5c5c"],
                other_current_screen_border=ocean["background"],
                other_screen_border=ocean["background"],
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
                    'green-background.png'
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
                    'yellow-green.png'
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
                    'purple-yellow.png'
                )
            ),
            widget.CurrentLayoutIcon(
                foreground=ocean["background"],
                background=ocean["purple"],
                scale=0.65
            ),
            widget.CurrentLayout(
                foreground=ocean["background"],
                background=ocean["purple"],
            ),
            widget.Sep(
                background=ocean["purple"],
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
                    'orange-purple.png'
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
                    'cyan-orange.png'
                )
            ),
            widget.TextBox(
                foreground=ocean["background"],
                background=ocean["cyan"],
                text=" "
            ),
            widget.Clock(
                foreground=ocean["background"],
                background=ocean["cyan"],
                padding=5,
                format='%d/%m/%Y - %I:%M %p'
            ),
            # widget.QuickExit(),
        ],
        30,
        background=ocean["background"][0],
        opacity=1,
    ),
)
