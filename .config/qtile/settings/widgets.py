from settings.screens.laptop import screen as laptop
from settings.screens.monitor import screen as monitor

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [laptop, monitor]
