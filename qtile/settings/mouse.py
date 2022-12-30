from libqtile.config import Drag, Click
from libqtile.command import lazy
from .keys import mod


mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button9", lazy.spawn("playerctl --ignore-player=chromium next")),
    Click([mod], "Button8", lazy.spawn("playerctl --ignore-player=chromium previous")),
    Click([mod], "Button6", lazy.spawn("playerctl --ignore-player=chromium play-pause"))
]
