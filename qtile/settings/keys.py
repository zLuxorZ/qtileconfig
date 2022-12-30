# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------
    # Switch between windows in current stack pane
    ([mod], "k", lazy.layout.down()),
    ([mod], "i", lazy.layout.up()),
    ([mod], "j", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod], "o", lazy.layout.grow()),
    ([mod], "u", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "i", lazy.layout.shuffle_up()),
    ([mod, "shift"], "k", lazy.layout.shuffle_down()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_left()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    #Rofi Themes https://github.com/adi1090x/rofi

    # Menu
    ([mod], "m", lazy.spawn("launcher_colorful")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("launcher_colorful_show")),

    # Browser
    ([mod], "e", lazy.spawn("brave")),

    # File Explorer
    ([mod], "a", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Spotify
    ([mod], "s", lazy.spawn("spotify")),

    # Notion
    ([mod], "f", lazy.spawn("notion-app")),

    # Discord
    ([mod], "d", lazy.spawn("discord")),

    # Code
    ([mod], "q", lazy.spawn("code")),

    # WPS
    ([mod], "r", lazy.spawn("libreoffice")),

    # Calculator
    ([], "XF86Calculator", lazy.spawn("qalculate-gtk")),

    # Screenshot
    ([], "Print", lazy.spawn("scrot /home/lluis/Imágenes/Screenshoots/captura-%m-%d-%y-%H:%M.png")),
    (["shift"], "Print", lazy.spawn("scrot -s /home/lluis/Imágenes/Screenshoots/captura-%m-%d-%y-%H:%M.png")),

    # ------------ Hardware Configs ------------

    # Screens
    ([mod], 'n', lazy.next_screen()),
    #([mod], 't', lazy.prev_screen()),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brighticon.sh  5%+")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brighticon.sh 5%-")),

    # Music
    ([], "XF86AudioNext", lazy.spawn("playerctl --ignore-player=chromium next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl --ignore-player=chromium previous")),
    ([], "XF86AudioPlay", lazy.spawn("playerctl --ignore-player=chromium play-pause")),

]]

