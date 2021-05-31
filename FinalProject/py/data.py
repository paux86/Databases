import mysql.connector
import random

db_session = mysql.connector.connect(
    host="ec2-34-207-191-240.compute-1.amazonaws.com",
    user="root",
    passwd="comp420",
    database="project"
)

cursor = db_session.cursor()

#cursor.execute(sql_cmd)
#response = cursor.fetchall()

first_names = ["Matt", "Mark", "Ryan", "Travis", "Andrew", "Brandon", "Eric", "Juliet", "Steve", "Mary", "Susan", "Lindsey", "Michelle"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Koptiar", "Jones", "Garcia", "Avery", "Stackhouse", "Miller", "Davis", "Martinez", "Rodriguez"]

names = []
for index in range(100):
    name = first_names[random.randint(0, len(first_names)-1)] + " " + last_names[random.randint(0, len(last_names)-1)]
    if name not in names:
        names.append(name)

street_names = ["First", "Second", "Third", "Forth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Park", "Main", "Oak", "Pine", "Maple", "Cedar", "Elm", "View", "Washington"]
street_suffix = ["St.", "Dr.", "Ln.", "Wy.", "Ct."]

addresses = []
for index in range(1000):
    number = random.randint(1,1000)
    street = street_names[random.randint(0, len(street_names)-1)]
    suffix = street_suffix[random.randint(0, len(street_suffix)-1)]
    address = "%s %s %s" % (number, street, suffix)
    
    if address not in addresses:
        addresses.append(address)

phone_numbers = []
for index in range(1000):
    number = random.randint(1000000, 9999999)
    if number not in phone_numbers:
        phone_numbers.append(number)

zips = []
for index in range(20):
    zipcode = random.randint(90000, 95000)
    if zipcode not in zips:
        zips.append(zipcode)

datetimes = []
for index in range(1000):
    datetime = "%d:%d:%d %d:%d:%d" % (2020, random.randint(1,12), random.randint(1,30), random.randint(0,23), random.randint(0,59), 0)
    if datetime not in datetimes:
        datetimes.append(datetime)

reminder_vals = [None, 7, 15, 30, 60, 90]

'''
customers = []
for index in range(200):
    customer = []
    customer.append(names[random.randint(0, len(names)-1)])
    customer.append(phone_numbers[random.randint(0, len(phone_numbers)-1)])
    customer.append(zips[random.randint(0, len(zips)-1)])
    customer.append(addresses[random.randint(0, len(addresses)-1)])
    #customer.append(datetimes[random.randint(0, len(datetimes)-1)])
    #customer.append(reminder_vals[random.randint(0, len(reminder_vals)-1)])

    if customer not in customers:
        customers.append(customer)

# insert customers
for customer in customers:
    cursor.callproc("addCustomer", customer)
    db_session.commit()
'''

'''
employees = []
for index in range(20):
    employee = []
    employee.append(names[random.randint(0, len(names)-1)])
    employee.append(phone_numbers[random.randint(0, len(phone_numbers)-1)])
    employee.append(zips[random.randint(0, len(zips)-1)])
    employee.append(addresses[random.randint(0, len(addresses)-1)])
    employee.append(random.randint(20,100))
    employee.append(datetimes[random.randint(0, len(datetimes)-1)])

    if employee not in employees:
        employees.append(employee)

# insert employees
for employee in employees:
    cursor.callproc("addEmployee", employee)
    db_session.commit()
'''

'''
appointments = []

for index in range(295):
    cust_id = random.randint(43,242)
    emp_id = random.randint(5,24)
    date = datetimes[random.randint(0, len(datetimes)-1)]
    cursor.execute("insert into `appointment` values (%s, %s, %s, %s, %s)", [None, cust_id, emp_id, None, date])
    db_session.commit()
'''

'''
suppliers = []
for index in range(20):
    sup_id = 2+index
    supplier = [sup_id, "Supplier %s" % (sup_id), phone_numbers[random.randint(0,len(phone_numbers))], "supplier%s@gmail.com" % (sup_id)]
    suppliers.append(supplier)

for supplier in suppliers:
    cursor.callproc("addSupplier", supplier)
    db_session.commit()
'''

'''
prefix = ["Generic", "Superior", "Epic"]
prod_id = 3
products = []

while len(products) < 50:
    name = "%s Product %s" % (prefix[random.randint(0,2)], random.randint(1,50))
    product = [prod_id, random.randint(1,21), name, random.randint(1,200), "%s does some stuff" % (name)]
    if product not in products:
        products.append(product)
        prod_id += 1

for product in products:
    cursor.callproc("addProduct", product)
    db_session.commit()
'''

'''
prefix = ["Generic", "Superior", "Epic"]
serv_id = 1
services = []

while len(services) < 25:
    name = "%s Service %s" % (prefix[random.randint(0,2)], random.randint(1,50))
    service = [serv_id, name, random.randint(1,200)]
    if service not in services:
        services.append(service)
        serv_id += 1

for service in services:
    cursor.callproc("addService", service)
    db_session.commit()
'''

'''
inventories = []

while len(inventories) < 100:
    emp_id = random.randint(5,24)
    prod_id = random.randint(1,52)
    quant = random.randint(1,100)
    inventory = [emp_id, prod_id, quant]

    if inventory not in inventories:
        inventories.append(inventory)

for inventory in inventories:
    cursor.callproc("addInventory", inventory)
    db_session.commit()
'''

'''
for index in range(50):
    cust_id = random.randint(43,242)
    emp_id = random.randint(5,24)
    invoice = [cust_id, emp_id]
    cursor.callproc("addCustomerInvoice", invoice)
    db_session.commit()
'''

'''
invoice_lines = []
while len(invoice_lines) < 150:
    inv_id = random.randint(21,70)
    prod_id = None
    serv_id = None
    inv_type = random.randint(1,2)
    if inv_type == 1:
        prod_id = random.randint(1,52)
    else:
        serv_id = random.randint(1,25)
    invoice = [inv_id, prod_id, serv_id]

    if invoice not in invoice_lines:
        invoice_lines.append(invoice)

for invoice in invoice_lines:
    invoice.append(random.randint(1,5))
    cursor.callproc("addCustomerInvoiceLine", invoice)
    db_session.commit()
'''


'''
for index in range(50):
    sup_id = random.randint(1,21)
    date = datetimes[random.randint(0, len(datetimes)-1)]
    cursor.execute("insert into `supplier_invoice` values (%s, %s, %s)", [None, sup_id, date])
    db_session.commit()
'''

'''
invoice_lines = []
while len(invoice_lines) < 150:
    inv_id = random.randint(4,53)
    prod_id = random.randint(1,52)
    quant = random.randint(5,25)
    invoice = [inv_id, prod_id, quant]

    if invoice not in invoice_lines:
        invoice_lines.append(invoice)

for invoice in invoice_lines:
    cursor.callproc("addSupplierInvoiceLine", invoice)
    db_session.commit()
'''

'''
payments = []
for index in range(150):
    inv_id = random.randint(21,70)
    amt = random.randint(10,100)
    payment = [inv_id, amt]
    payments.append(payment)

for payment in payments:
    cursor.callproc("addPayment", payment)
    db_session.commit()
'''