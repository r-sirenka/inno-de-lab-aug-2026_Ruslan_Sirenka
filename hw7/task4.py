requested_roles = ["guest", "developer", "guest", "admin",
"developer", "guest"]
required_admin_roles = {"admin", "security_officer",
"audit_manager"}

requested_roles_set = set(requested_roles)

common_roles = requested_roles_set & required_admin_roles

missing_roles = required_admin_roles - requested_roles_set

security_officer_present = "security_officer" in requested_roles_set

print(f"Уникальные запрошенные роли: {requested_roles_set}")
print(f"Общие административные роли: {common_roles}")
print(f"Недостающие административные роли: {missing_roles}")
print(f"Наличие роли security_officer в запросе: {security_officer_present}")