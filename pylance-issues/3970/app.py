# SCENARIO: a nested Flask route handler inside an app factory is marked as unaccessed while the top-level route handler is not
# TARGET: `nested_route` inside `create_app` below
# TRIGGER: open this file with Pylance analysis enabled and inspect unused-code diagnostics on both route handlers
# EXPECT: `top_level_route` stays clean while `nested_route` is the only route handler flagged as unused or unaccessed
# VERIFY: if `nested_route` is reported unused while `top_level_route` is not, the current strongest screenshot-consistent hypothesis still reproduces
# RECOVER: no recovery needed
# NOTE: this retained repro models the strongest current hypothesis for microsoft/pylance-release#3970; it is not claimed to be the exact original reporter snippet

# pyright: strict
from flask import Flask

app = Flask(__name__)


@app.route('/')
def top_level_route() -> str:
    return 'top'


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def nested_route() -> str:
        return 'nested'

    return app


application = create_app()