db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

db_connection = db_config.get("connection")
db_host = db_connection.get("host")
db_port = db_connection.get("port")

ssl_settings = db_connection.get("ssl_settings", None)
if ssl_settings is None:
    db_ssl_mode = "verify-full"
else:
    db_ssl_mode = ssl_settings.get("ssl_mode", "verify-full")

## db_ssl_settings = db_connection.get("ssl_settings", {})     
## db_ssl_mode = db_ssl_settings.get("ssl_mode", "verify-full") 
## не знаю какой вариант лучше и правильнее - это тот же подпункт 2

db_connection["user"] = "admin"

db_connection["max_connections"] = 100

print(f"SSL Mode: {db_ssl_mode}")
print("Параметры соединения:")
for k, v in db_connection.items():
    print(f"* {k}: {v}")

