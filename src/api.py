from fastapi import FastAPI
import os
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

api = FastAPI(
    title="api to test the render platform"
)

FastAPIInstrumentor.instrument_app(api)
exporter = OTLPMetricExporter(endpoint="otlp-gateway-prod-us-east-2.grafana.net/otlp", headers={"Authorization": f"Bearer {os.getenv("GRAFANA_TOKEN")}"})
reader = PeriodicExportingMetricReader(exporter=exporter, export_interval_millis=5000)
provider = MeterProvider(metric_readers=[reader])

@api.get("/hello")
def say_hello():
    return {
        "msg": "render version 2!"
    }