sueldo_bruto = int(input("Ingresa sueldo bruto: "))

desc_salud = sueldo_bruto * 0.07
desc_seguro = sueldo_bruto * 0.006
desc_afp = sueldo_bruto * 0.10

descuentos = desc_salud + desc_seguro + desc_afp
sueldo_liquido = sueldo_bruto - descuentos

print(f"Sueldo bruto \t {sueldo_bruto:,.0f}")
print(f"Desc salud \t {desc_salud:,.0f}")
print(f"Desc seguro \t {desc_seguro:,.0f}")
print(f"Desc afp \t {desc_afp:,.0f}")
print(f"Sueldo liquido \t {sueldo_liquido:,.0f}")
