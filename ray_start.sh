# https://docs.ray.io/en/latest/cluster/vms/user-guides/launching-clusters/on-premises.html
# start head at `device0`
# pip install -U "ray[default]"
ray start --head \
    --dashboard-host 0.0.0.0 --dashboard-port 8265 --include-dashboard True \
    --port 8266

# connect to Ray runtime at `device1` & `device2`
# pip install -U "ray[default]"
# NOTE: ip may differ
ray start --address='192.168.2.164:8266'

# monitor
# 192.168.2.164:8265
