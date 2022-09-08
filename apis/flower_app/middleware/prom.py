from prometheus_client import CollectorRegistry, generate_latest
from prometheus_client import Counter, Histogram
import time


class PrometheusMiddleware(object):
    def __init__(self):
        self.registry = CollectorRegistry()
        self.requests = Counter(
            'http_total_request',
            'Counter of total HTTP requests',
            ['method', 'path', 'status'],
            registry=self.registry)

        self.request_historygram = Histogram(
            'request_latency_seconds',
            'Histogram of request latency',
            ['method', 'path', 'status'],
            registry=self.registry)

    def process_request(self, req, resp):
        req.start_time = time.time()

    def process_response(self, req, resp, resource, req_succeeded):
        resp_time = time.time() - req.start_time

        self.requests.labels(method=req.method,
                             path=req.path,
                             status=resp.status).inc()
        self.request_historygram.labels(
            method=req.method,
            path=req.path,
            status=resp.status).observe(resp_time)

    def on_get(self, req, resp):
        data = generate_latest(self.registry)
        resp.content_type = 'text/plain; version=0.0.4; charset=utf-8'
        resp.body = str(data.decode('utf-8'))
