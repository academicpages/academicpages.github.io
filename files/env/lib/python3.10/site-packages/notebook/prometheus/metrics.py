"""
Prometheus metrics exported by Jupyter Notebook Server

Read https://prometheus.io/docs/practices/naming/ for naming
conventions for metrics & labels.
"""


from prometheus_client import Histogram, Gauge


HTTP_REQUEST_DURATION_SECONDS = Histogram(
    'http_request_duration_seconds',
    'duration in seconds for all HTTP requests',
    ['method', 'handler', 'status_code'],
)

TERMINAL_CURRENTLY_RUNNING_TOTAL = Gauge(
    'terminal_currently_running_total',
    'counter for how many terminals are running',
)

KERNEL_CURRENTLY_RUNNING_TOTAL = Gauge(
    'kernel_currently_running_total',
    'counter for how many kernels are running labeled by type',
    ['type']
)
