from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left 
        fontsize=37,
        padding=-3
    )


def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=17,
            margin_y=2,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5, max_chars=30),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color5', 'dark'),
    
    icon(bg="color5", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color5'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0 ',
        display_format='{updates} ',
        update_interval=300,
        custom_command='checkupdates+aur',
    ),

    powerline('color4', 'color5'),

    icon(bg="color4", text=''),

    widget.CryptoTicker(**base(bg='color4'), crypto='BTC', currency='USD', update_interval=30, format='${amount:.0f}', fmt=' {} '),

    widget.Mpris2(**base(bg='color4'), name='spotify', objname="org.mpris.MediaPlayer2.spotify", fmt='|   {} ', display_metadata=['xesam:title'], scroll_chars=None, stop_pause_text='', no_metadata_text='', scroll_wait_intervals=0, max_chars=20),
    
    widget.Mpd2(**base(bg='color4'), host='127.0.0.1', status_format='{play_status} {title}', idle_format='', play_states={'pause': ' ', 'play': ' ', 'stop': ' '}, update_interval=0.5, no_connection='', fmt='| {} ', max_chars=20),

    powerline('color3', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5, fmt='{}'),

    powerline('color2', 'color3'),

    icon(bg="color2", text=' '),
    
    widget.CPU(**base(bg='color2'), format='CPU: {load_percent}% | '),

    icon(bg="color2", text='﬙ '),

    widget.Memory(**base(bg='color2'), measure_mem='G', format= 'RAM:{MemUsed: .0f}{mm} '),

    powerline('color1', 'color2'),

    widget.Systray(background=colors['color1'], padding=5),

    widget.Backlight(background=colors['color1'], padding=2,step=5, fmt='  ', change_command='brighticon.sh {0}%', brightness_file='/sys/class/backlight/intel_backlight/actual_brightness', max_brightness_file='/sys/class/backlight/intel_backlight/max_brightness'),

    widget.Spacer(background=colors['color1'], length=4),

    widget.Clock(**base(bg='color1'), format='- [ %d/%m/%y | %H:%M ] -'),

    widget.TextBox(**base(bg='color1'), text='Lluís -', padding=5),

    widget.LaunchBar(background=colors['color1'], progs=[('bash', 'poweroff', 'SHUTDOWN')], default_icon='/home/lluis/.config/qtile/icons/shutdown.png', padding=0),

    widget.Spacer(background=colors['color1'], length=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color3', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color2', 'color3'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
