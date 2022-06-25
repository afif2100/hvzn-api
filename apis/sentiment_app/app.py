import falcon
from helper.health import HealthCheck
from api.hello_name import HelloName
from middleware import PrometheusMiddleware

prometheus = PrometheusMiddleware()
app = falcon.App(middleware=prometheus)
health = HealthCheck()
Name = HelloName()

# endpoint
endpoint_prefix = "api/v1"

# app route
app.add_route('/health', health)
app.add_route(f'/{endpoint_prefix}/hello', Name)

# metrics collector
app.add_route('/metrics', prometheus)
