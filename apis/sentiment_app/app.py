import falcon
from helper.health import HealthCheck
from api.sentiment import Sentiment
from middleware import PrometheusMiddleware

prometheus = PrometheusMiddleware()
app = falcon.App(middleware=prometheus)
health = HealthCheck()
sentiment = Sentiment()

# endpoint
endpoint_prefix = "api/v1"

# app route
app.add_route("/health", health)
app.add_route(f"/{endpoint_prefix}/sentiment", sentiment)

# metrics collector
app.add_route("/metrics", prometheus)
