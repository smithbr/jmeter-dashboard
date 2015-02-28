from jmd import login_manager
from jmd.config import config
from jmd.model.user import UserObj

# Login configuration
login_manager.login_view = config.LOGIN_VIEW


@login_manager.user_loader
def load_user(userid):
    """
    This loads a user
    """
    return UserObj.get(userid)
