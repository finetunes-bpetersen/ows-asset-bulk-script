from flask import Flask

from asset_bulk_script.api import app
from asset_bulk_script import asset_import_controller
from asset_bulk_script import config

@app.route('/')
def hello_world():
    return 'Asset Bulk Script'


if __name__ == '__main__':
    app.run()
