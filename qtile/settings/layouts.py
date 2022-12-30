from libqtile import layout
from libqtile.config import Match
from .theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': "#c4c4c4",
    'border_width': 2,
    'border_normal': "#2C2C2C",
    'grow_amount': 20,
    'margin': 7
}

layouts = [
    layout.Stack(**layout_conf, num_stacks=1),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf, align=0),
    #layout.MonadWide(**layout_conf, align=0),
    #layout.Max(),
    #layout.Bsp(**layout_conf),
    #layout.MonadThreeCol(**layout_conf, align=0, main_centered=False, new_client_position='bottom'),
    #layout.Spiral(**layout_conf),
    #layout.Floating(**layout_conf),
    #layout.Matrix(columns=2, **layout_conf),
    #layout.RatioTile(**layout_conf),
    #layout.Columns(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='catfish'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
	Match(wm_class='Msgcompose'),
	Match(wm_class='codelite-terminal'),
	Match(wm_class='Xfce4-terminal'),
    ],
    border_focus=colors["color4"][0]
)


