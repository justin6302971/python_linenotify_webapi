import multiprocessing

bind = "0.0.0.0:8000"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
worker_class='sync'
timeout=7200

# reload=True# for debugging