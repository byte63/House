# import os
# import sys
# sys.path.append(os.path.basename(os.path.basename(__file__)))

from flask import render_template
from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app

# env = os.environ.get("python_env", "develop")
env = "develop"

app = create_app(env)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()
