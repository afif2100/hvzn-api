import falcon
from helper.health import HealthCheck
from api.hello_name import HelloName
from middleware import PrometheusMiddleware
from api.FlowerApp import FlowerPrediction

prometheus = PrometheusMiddleware()
app = falcon.App(middleware=prometheus)
health = HealthCheck()
Name = HelloName()
flower = FlowerPrediction()

# endpoint
endpoint_prefix = "api/v1"

# app route
app.add_route('/health', health)
app.add_route(f'/{endpoint_prefix}/hello', Name)
app.add_route(f'/{endpoint_prefix}/predict', flower)


# metrics collector
app.add_route('/metrics', prometheus)
