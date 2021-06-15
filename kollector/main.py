# from app import create_app
# app = create_app()

from app.models import Note
from app import create_app

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

manager = Manager(create_app)

manager.add_command("runserver",
                    Server(host='0.0.0.0',
                           port=5000,
                           use_debugger=True))


@manager.command
def save_todo():
    todo = Note(content="my first todo")
    todo.save()


if __name__ == '__main__':
    manager.run()
