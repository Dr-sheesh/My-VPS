import psutil

# CPU Usage
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

# Memory Usage
memory = psutil.virtual_memory()
print("Memory Usage:", memory.percent, "%")
print("Total Memory:", memory.total // (1024 ** 2), "MB")
print("Available Memory:", memory.available // (1024 ** 2), "MB")

# Disk Usage
disk = psutil.disk_usage('/')
print("Disk Usage:", disk.percent, "%")
print("Total Disk Space:", disk.total // (1024 ** 3), "GB")
print("Free Disk Space:", disk.free // (1024 ** 3), "GB")

# Network Usage
net = psutil.net_io_counters()
print("Bytes Sent:", net.bytes_sent // (1024 ** 2), "MB")
print("Bytes Received:", net.bytes_recv // (1024 ** 2), "MB")
