production = False

if production:
    from .herokusettings import *
else:
    from .devsettings import *
