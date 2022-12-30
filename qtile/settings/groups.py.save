# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import mod, keys

import time

groups = []

for i in ["   ", "   ", "   ", "  ", "   ", "   ", " 阮  ", "   "]:
    if i == "   ":
        groups.append(Group(i, layout="stack",      matches=[Match(wm_class=["brave-browser"])]))
    elif i == "   ":
        groups.append(Group(i, layout="monadwide"))
    elif i == "   ":
        groups.append(Group(i, layout="stack",     matches=[Match(wm_class=["code-oss"])]))
    elif i == "  ":
        groups.append(Group(i, layout="monadtall", matches=[Match(wm_class=["thunderbird","notion-app", "cpupower-gui", "nvidia-settings"])]))
    elif i == "   ":
        groups.append(Group(i, layout="monadtall", matches=[Match(wm_class=["Thunar"])]))
    elif i == "   ":
        groups.append(Group(i, layout="stack",     matches=[Match(wm_class=["libreoffice"], title=["LibreOffice"])]))
    elif i == " 阮  ":
        groups.append(Group(i, layout="monadtall", matches=[Match(wm_class=["Spotify", "discord", "pavucontrol", "whatsapp-nativefier-d40211"])]))
    elif i == "   ":
        groups.append(Group(i, layout="stack",     matches=[Match(wm_class=["Steam", "csgo_linux64"])]))
    else:
        groups.append(Group(i, layout="stack"))

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
