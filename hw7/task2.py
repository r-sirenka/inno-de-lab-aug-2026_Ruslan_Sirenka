raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10",
"SUCCESS:0", "SUCCESS:250", "ERROR:200"]
filtered_transactions = [
    int(t.split(":")[1]) 
    for t in raw_transactions 
    if t.startswith("SUCCESS") and int(t.split(":")[1]) > 0
]
print(f"Очищенные транзакции: {filtered_transactions}")