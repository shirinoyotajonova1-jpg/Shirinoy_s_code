#1. Collect Customer Information 
customer_name = input(" Enter customer name:  ")
has_student_id_input = input("Does customer have student ID? (yes/no) : "). strip(). lower()
has_student_id = has student_id_input == "yes"
order_time = int(input("enter order time(hour in 24 hour format, e.g., 13 for 1pm)"))

# 2. Collect 3 dishes Information
print(f"\ n--- Dish {i} ---")
dish_name = input(f"Enter dish {i} name: ")
price= float(input(f"Enter dish {i} price: "))
quantity = int(input(f"Enter quantity:  "))
orders.append("name": dish_name, "price": price, "quantity": quantity})

#3. Calculate Subtotal before discounts
subtotal_before_discounts = sum(item["price"]) item["quantity"] for item in orders)

#4. Discount Eligibility and Amounts
# Student discount: 15% off subtotal 
is_student_eligible = has_student_id
student_discount_amount = subtotal_before_discounts * 0.15 if is_student_elgible else 0.0
#Hour hour discount :20 % off subtotal (14 <=order_time <=17)
is_happy_hour_eligible = 14 <=order_time <= 17
happy_hour_discount_amount =subtotal_before_discounts * 0.20 if is_happy_houreligbile esle 0.0
#Non-stacking Main Discount calculation using given formula:
main_discount = (student_discountamount * (student_discount_amount >= happy_hour_discount_amount) + happy_hour_discount_amount * (happy_hour_discount_amount > student_discount_amount))
   #Determine which discount was applied for display
                  if main_discount > 0:
                    if student_discount_amount >= happy_hour_discount_amount:
       applied_main_discount_name = "Student Discount"
                 else:
                                 applied_main_discount_name = "happy Hour Discount"
                            else:
applied_main_discount_name = "None"

#Large order discount: 5% off subtotal if subtotal >= 150000
is_large_order_eligible = subtotal_before_discount * 0.05 if is_large_order_eligible else 0.0

#Total discount and subtotal after discounts
total_disconts =main_discounts+large_order_discount_amount
subtotal_after_discounts =subtotal_before_discounts - total_disconts

#5. Other Calculations

delivery_fee =int(subtotal_before_discounts >= 100000) * 15000
is_free_delivery = delivery_fee == 0

#Final total&total amount saved 
final_total = subtotal_after_discounts +service_charge +delivery_fee
total_amount_saved =total_discounts

#======================================
#OUTPUT 
#======================================
print("n\"+"="="*45)
print("          ORDER RECIEPT           ")
print("="*45)

#Customer Info
print(f"Customer Name: {customer_name}")
print(f"Student Status: { has_student_id}")
print(if"Order Time: {order_time}: 00")
print("45")
#Itemized list of 3 orders
print("Itemized Orders:")
for Item in orders:
    item_tootal=item["price"] * item["quantity"]

    print("-" *45)
    #Discounts Breakdown:")
    print("Disconts Breakdown:")"
    print(f" -Student DIscount Eligiblity: {is_student_eligible} |Amount: {student_discount_aount:.2f}")
    print(f" -Happy Hour Eligibilty: {is_happy_hour_eligible} |Amont: {happy_hour_discount:.2f}")
    print(f"-Applied Main discount : {applied_main_discount_name}  ({main_discount:.2f})")
    print(f" -Large Order Eligibility: {is_large_order_eligble  |Amount: {large_order_discount_amount:.2f}")"}
    ")print(f"Total Discounts": {total_discounts: .f")")
    "})
    #Service Charge &Delivery fee
    print("Service CHarge (10%): {service_charge:.2f}")
    print(f"Delivery Fee:{delivery_fee:.2f} (Fee Delivery:  {is_free_delivery})")
    print("-" *45)

    #Final Totals
    print(f"FINAL TOTAL:{final_total:2f.}")
    print(f"TOTAL AMOUNT SAVED: {total_amount_saved:.2f}")
    print("="*45)
