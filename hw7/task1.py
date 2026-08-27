raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
elements = raw_user_record.split(';')
user_id = elements[0].strip()
name = elements[1].strip()
city = elements[2].strip()
status = elements[3].strip()
user_id = f"UID-{user_id}"
name = name.replace("_", " ")
name = name.title()
city = city.upper()
status = status.lower()
all_elements = [user_id, name, city, status]
result = " | ".join(all_elements)
print(f"Нормализованная запись: {result}")