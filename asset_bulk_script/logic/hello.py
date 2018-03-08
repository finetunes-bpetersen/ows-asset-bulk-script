"""Logic for Hello.
Verify that the application and its dependencies are available.
"""

from oto import response

from sqlalchemy.exc import SQLAlchemyError

from asset_bulk_script.api import db


def health_check():
    """Health check handler.
    Checks database connection. 200 if OK, otherwise 503 service unavailable.
    Returns:
        Response: the system status.
    """
    try:
        db.execute("SELECT * FROM label_status");
    except SQLAlchemyError as err:
        print("OS error: {0}".format(err))
        return response.create_error_response(
            code='Internal Server Error',
            message='could not connect to psql',
            status=503)

    return response.Response(message={'status': 'ok'}, status=200)