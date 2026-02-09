def check_access(age):
    if age >= 18:
        return "Доступ дозволено"
    else:
        return "Доступ заборонено"

print(check_access(15))