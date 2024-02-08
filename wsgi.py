# -*- coding: utf-8 -*-
"""Create an application instance."""
from app.www_launcher import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
