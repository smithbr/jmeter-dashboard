from flask_debugtoolbar import DebugToolbarExtension

from jmd import app


if __name__ == '__main__':
    app.debug = True

    if app.debug is True:
        toolbar = DebugToolbarExtension(app)

    app.run()
