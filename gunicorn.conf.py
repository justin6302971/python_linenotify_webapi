import multiprocessing

bind = "127.0.0.1:8080"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
worker_class='sync'
timeout=7200

reload=True# for debugging