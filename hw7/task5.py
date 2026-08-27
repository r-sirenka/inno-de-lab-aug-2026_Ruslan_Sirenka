system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]

active_nodes = []
cpu_loads = []
ram_usages = []

for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "offline":
        continue
    active_nodes.append(node_name)
    cpu_loads.append(cpu_load)
    ram_usages.append(ram_usage)
active_nodes_count = len(active_nodes)
average_cpu = round(sum(cpu_loads) / len(cpu_loads), 2)
max_ram = max(ram_usages)

final_report = {
    "active_nodes_count": active_nodes_count,
    "metrics": {
        "average_cpu": average_cpu,
        "max_ram": max_ram
    }
}

print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчет телеметрии:")
## print(final_report) - это как я делал изначально, но было не как в примере визуально
print("{")
for key, value in final_report.items():
    if isinstance(value, dict):
        print(f"    '{key}': {{")
        for sub_key, sub_value in value.items():
            print(f"        '{sub_key}': {sub_value}")
        print("    }")
    else:
        print(f"    '{key}': {value}")
print("}")
## посмотрел, что можно еще так сделать, чтобы было точно как в примере, но не знаю насколько радионально 