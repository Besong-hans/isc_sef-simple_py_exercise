def calculate_total_bill(amount_spent, is_loyal_customer):
   
    discount = 0
    service_charge = 0
    
    if amount_spent > 10000:
        discount = 0.20  # 20% discount for spending over 10,000
        if is_loyal_customer:
            discount += 0.05  # Additional 5% discount for loyalty members
    elif not is_loyal_customer:
        service_charge = 0.05  # 5% service charge if not a loyalty member and under 10,000
    
    final_amount = amount_spent * (1 - discount) * (1 + service_charge)
    return round(final_amount, 2)

print(calculate_total_bill(12000, True)) 
print(calculate_total_bill(12000, False)) 
print(calculate_total_bill(9000, True))   
print(calculate_total_bill(9000, False))  