from backmeup.server import app
import os
from pathlib import Path
from backmeup.util import init as db_init
if __name__ == '__main__':
    app.secret_key = os.urandom(24).hex()
    app.config['SESSION_TYPE'] = 'filesystem'
    UPLOAD_FOLDER = Path("/app/data")
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    db_init(app)
    app.run(        
        host="0.0.0.0",
        port=8000,
        debug=True,)
