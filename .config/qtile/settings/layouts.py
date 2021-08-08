from libqtile import layout
from libqtile.config import Match


layout_conf = {
    'border_focus': '#009688',
    'border_width': 1,
    'margin': 4
}

layouts = [
    # layout.Columns(border_focus_stack='#009688'),
    layout.Max(),
    # Pruebe más diseños desatando los siguientes diseños.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


floating_layout = layout.Floating(float_rules=[
    # Ejecute la utilidad de `xprop` para ver la clase wm y el nombre de un
    # cliente X.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], border_focus='#a151d3')
