from os import path

from libqtile import bar, widget
from libqtile.config import Screen

from settings.path import qtile_path


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
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#263238", "#263238"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#607D8B", "#607D8B"],
                    rounded=False,
                    highlight_method='block',
                    this_current_screen_border=["#009688", "#009688"],
                    this_screen_border=["#5c5c5c", "#5c5c5c"],
                    other_current_screen_border=["#263238", "#263238"],
                    other_screen_border=["#263238", "#263238"]
                ),
                # widget.Prompt(),
                widget.WindowName(
                    foreground=["#009688", "#009688"],
                    background=["#263238", "#263238"],
                    font='UbuntuMono Nerd Font Bold',
                    fontsize=14,
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox(
                #     "Press &lt;M-r&gt; to spawn", foreground="#d75f5f"
                # ),
                widget.Systray(),
                widget.Sep(
                    background=["#263238", "#263238"],
                    linewidth=0,
                    padding=5
                ),

                # Wheather
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material-ocean',
                        'images',
                        'bar4.png'
                    )
                ),
                widget.TextBox(
                    foreground=["#263238", "#263238"],
                    background=["#c3e88d", "#c3e88d"],
                    text="摒 "
                ),
                widget.OpenWeather(
                    foreground=["#263238", "#263238"],
                    background=["#c3e88d", "#c3e88d"],
                    app_key='ceefe984e6ae8ea8d01560b967bd3a78',
                    cityid='3688689',
                    format='{location_city}: {main_temp} °{units_temperature} {humidity}% {weather_details}',
                    language='es'
                ),
                widget.Sep(
                    background=["#c3e88d", "#c3e88d"],
                    linewidth=0,
                    padding=5
                ),

                # NET GRAPH
                # widget.Image(
                #     filename=path.join(
                #         qtile_path,
                #         'themes',
                #         'material-ocean',
                #         'images',
                #         'bar4.png'
                #     )
                # ),
                # widget.TextBox(
                #     foreground=["#263238", "#263238"],
                #     background=["#f78c6c", "#f78c6c"],
                #     text="龍 "
                # ),
                # widget.Net(
                #     foreground=["#263238", "#263238"],
                #     background=["#f78c6c", "#f78c6c"]
                # ),
                # widget.NetGraph(
                #     background=["#f78c6c", "#f78c6c"],
                #     border_color='f78c6c',
                #     fill_color='f78c6c',
                #     graph_color='263238',
                #     line_width=2
                # ),
                # widget.Sep(
                #     background=["#f78c6c", "#f78c6c"],
                #     linewidth=0,
                #     padding=5
                # ),

                # UPDATES
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material-ocean',
                        'images',
                        'bar3.png'
                    )
                ),
                widget.TextBox(
                    foreground=["#263238", "#263238"],
                    background=["#ffcb6b", "#ffcb6b"],
                    text=" "
                ),
                widget.CheckUpdates(
                    foreground=["#263238", "#263238"],
                    background=["#ffcb6b", "#ffcb6b"],
                    colour_have_updates='#263238',
                    colour_no_updates='#263238',
                    display_format='{updates}',
                    no_update_string='N/A',
                    custom_command='checkupdates',
                    update_interval=1800
                ),
                widget.Sep(
                    background=["#ffcb6b", "#ffcb6b"],
                    linewidth=0,
                    padding=5
                ),

                # LAYOUT
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material-ocean',
                        'images',
                        'bar2.png'
                    )
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#263238", "#263238"],
                    background=["#f07178", "#f07178"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#263238", "#263238"],
                    background=["#f07178", "#f07178"],
                ),
                widget.Sep(
                    background=["#f07178", "#f07178"],
                    linewidth=0,
                    padding=5
                ),

                # FECHA Y HORA
                widget.Image(
                    filename=path.join(
                        qtile_path,
                        'themes',
                        'material-ocean',
                        'images',
                        'bar1.png'
                    )
                ),
                widget.TextBox(
                    foreground=["#263238", "#263238"],
                    background=["#82aaff", "#82aaff"],
                    text=" "
                ),
                widget.Clock(
                    foreground=["#263238", "#263238"],
                    background=["#82aaff", "#82aaff"],
                    padding=5,
                    format='%d/%m/%Y - %a %I:%M %p'
                ),
                # widget.QuickExit(),
            ],
            24,
            background='#263238',
            opacity=0.95,
        ),
    ),
]
