"""Flask and other extensions instantiated here.

To avoid circular imports with views and create_app(), extensions are instantiated here. They will be initialized
(calling init_app()) in application.py.
"""

from logging import getLogger

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from sqlalchemy.event import listens_for
from sqlalchemy.pool import Pool

LOG = getLogger(__name__)


@listens_for(Pool, 'connect', named=True)
def _on_connect(dbapi_connection, **_):
    """Set MySQL mode to TRADITIONAL on databases that don't set this automatically.

    Without this, MySQL will silently insert invalid values in the database, causing very long debugging sessions in the
    long run.
    http://www.enricozini.org/2012/tips/sa-sqlmode-traditional/
    """
    LOG.debug('Setting SQL Mode to TRADITIONAL.')
    dbapi_connection.cursor().execute("SET SESSION sql_mode='TRADITIONAL'")

db = SQLAlchemy()
mail = Mail()
csrf = CsrfProtect()

