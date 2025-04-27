from flask import Flask
from flask_cors import CORS
from strawberry.flask.views import GraphQLView
from schema import schema

app = Flask(__name__)
CORS(app)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True)
