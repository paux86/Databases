# Matt Brierley
# Comp 420
# Fall 2020

import mysql.connector
import tkinter as tk
from PIL import Image, ImageTk

'''
TODO:
remove col headers from scroll box (without breaking the grid)
fix refine bug (refining a refined query appends a second where clause, returning nothing)

= nice to haves =
-delete invoice (run delete on each line procedurally in sql?)
-tranfer product between inventories
-link customer lookup to add new appointment - autofill parameters
-view schedule from employee view (can refine on employee id for now)
'''

db_session = mysql.connector.connect(
    host="ec2-34-207-191-240.compute-1.amazonaws.com",
    user="root",
    passwd="comp420",
    database="project"
)

cursor = db_session.cursor()

WIDTH = 1515
HEIGHT = 760
BG_COLOR = '#f2f2f2'
BG2_COLOR = '#ffffff'
ENTRY_WIDTH = 16
# hacky fixes, hopefully temp.
col_headers = []
open_invoice = None
last_ran_cmd_paramList = None

insert_params = {
    "appointment" : ["addAppointment", "Customer Id", "Employee Id", "Description", "Date"],
    "product" : ["addProduct", "Id", "Supplier Id", "Name", "Cost per unit", "Description"],
    "supplier" : ["addSupplier", "Id", "Name", "Phone #", "Email"],
    "inventory" : ["addInventory", "Employee Id", "Product Id", "Quantity"],
    "customer" : ["addCustomer", "Name", "Phone #", "Zip", "Address"],
    "employee" : ["addEmployee", "Name", "Phone", "Zip", "Address", "Hourly Rate", "Start Date"],
    "customerInvoice" : ["addCustomerInvoice", "Customer Id", "Employee Id"],
    "customerInvoiceLine" : ["addCustomerInvoiceLine", "Product Id", "Service Id", "Quantity"],
    "supplierInvoice" : ["addSupplierInvoice", "Supplier Id"],
    "supplierInvoiceLine" : ["addSupplierInvoiceLine", "Product Id", "Quantity"],
    "payment" : ["addPayment", "Invoice Id", "Payment Amount"]
}

row_modifiers = {
    "appointment" : [["Update", "updateAppointment", [0,1,6,8,9], [0,2,3,4,5,7]], ["Delete", "deleteAppointment", [0]]],
    "product" : [["Update", "updateProduct", list(range(5)), [0]]],
    "supplier" : [["Update", "updateSupplier", list(range(4)), [0]]],
    "inventory" : [["Update", "updateInventory", [0,2,5], [0,1,2,3,4]]],
    "customer" : [["Update", "updateCustomer", list(range(7)), [0]]],
    "unbilledCustomers" : [["Billed", "customerBilled", [3], [6]]],
    "employee" : [["Update", "updateEmployee", list(range(8)), [0]]],
    "customer_invoice" : [["View", "getCustomerInvoice", [], [0,1,2,3,6]]],
    "customer_invoice_line" : [["Update", "updateCustomerInvoiceLine", [0,1,2,4,6,7], [0,1,3,5,7]], ["Delete", "deleteCustomerInvoiceLine", [0,1,2,4,6,7]]],
    "supplier_invoice" : [["View", "getSupplierInvoice", [], [0,1,2]]],
    "supplier_invoice_line" : [["Update", "updateSupplierInvoiceLine", [0,1,2,4], [0,1,3]], ["Delete", "deleteSupplierInvoiceLine", [0,1,2,4]]]
}

def clear_widgets():
    for widget in root.winfo_children():
        if widget is not canvas:
            widget.destroy()

def main_menu():
    clear_widgets()
    # create navigation buttons
    nav_button_relX = .25
    nav_button_rely = .5
    navbutton_relwidth = .1
    navbutton_relheight = .05
    appointments_button = tk.Button(root, text="Appointments", command=lambda: appointments_menu())
    appointments_button.place(relwidth=navbutton_relwidth, relheight=navbutton_relheight, rely=nav_button_rely, relx=nav_button_relX)
    products_button = tk.Button(root, text="Products", command=lambda: products_menu())
    products_button.place(relwidth=navbutton_relwidth, relheight=navbutton_relheight, rely=nav_button_rely, relx=nav_button_relX + navbutton_relwidth)
    clients_button = tk.Button(root, text="Customers", command=lambda: clients_menu())
    clients_button.place(relwidth=navbutton_relwidth, relheight=navbutton_relheight, rely=nav_button_rely, relx=nav_button_relX + (navbutton_relwidth * 2))
    employees_button = tk.Button(root, text="Employees", command=lambda: employees_menu())
    employees_button.place(relwidth=navbutton_relwidth, relheight=navbutton_relheight, rely=nav_button_rely, relx=nav_button_relX + (navbutton_relwidth * 3))
    invoice_button = tk.Button(root, text="Invoice", command=lambda: invoice_menu())
    invoice_button.place(relwidth=navbutton_relwidth, relheight=navbutton_relheight, rely=nav_button_rely, relx=nav_button_relX + (navbutton_relwidth * 4))

def appointments_menu():
    clear_widgets()
    title_text = tk.Label(root, text="Appointments", font=('Helvetica', 12, 'bold'), bg=BG2_COLOR).place(relx=0.125, rely=0.17, relwidth=0.1, anchor='n')

    appointments_query = query_display(root, cursor, "Select * from allAppointments", None, True, insert_params["appointment"], row_modifiers["appointment"])
    selector_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
    selector_frame.place(relx=0.125, rely=0.2, relwidth=0.1, relheight=0.6, anchor='n')
    home_button = tk.Button(selector_frame, text="Home", bg='#6666ff', command=lambda: main_menu())
    home_button.place(relwidth=1, relheight=1/6, rely=0)
    dayView_button = tk.Button(selector_frame, text="View All", command=lambda: appointments_query.run_and_display("Select * from allAppointments", None, True, insert_params["appointment"], row_modifiers["appointment"]))
    dayView_button.place(relwidth=1, relheight=1/6, rely=2/6)
    unassignedView_button = tk.Button(selector_frame, text="Unassigned", command=lambda: appointments_query.run_and_display("Select * from unassignedAppointments", None, False, None, row_modifiers["appointment"]))
    unassignedView_button.place(relwidth=1, relheight=1/6, rely=3/6)
    dayView_button = tk.Button(selector_frame, text="Today", command=lambda: appointments_query.run_and_display('getAppointments', [None, None, None], False, None, None))
    dayView_button.place(relwidth=1, relheight=1/6, rely=4/6)
    weekView_button = tk.Button(selector_frame, text="7 Day", command=lambda: appointments_query.run_and_display('getAppointments', [7, None, None], False, None, None))
    weekView_button.place(relwidth=1, relheight=1/6, rely=5/6)

def products_menu():
    clear_widgets()
    title_text = tk.Label(root, text="Products", font=('Helvetica', 12, 'bold'), bg=BG2_COLOR).place(relx=0.125, rely=0.17, relwidth=0.1, anchor='n')

    products_query = query_display(root, cursor, 'SELECT * from allProducts', None, True, insert_params["product"], row_modifiers["product"])
    selector_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
    selector_frame.place(relx=0.125, rely=0.2, relwidth=0.1, relheight=0.6, anchor='n')
    home_button = tk.Button(selector_frame, text="Home", bg='#6666ff', command=lambda: main_menu())
    home_button.place(relwidth=1, relheight=1/6, rely=0)
    products_button = tk.Button(selector_frame, text="Products", command=lambda: products_query.run_and_display('SELECT * from allProducts', None, True, insert_params["product"], row_modifiers["product"]))
    products_button.place(relwidth=1, relheight=1/6, rely=1/6)
    suppliers_button = tk.Button(selector_frame, text="Suppliers", command=lambda: products_query.run_and_display('SELECT * from allSuppliers', None, False, insert_params["supplier"], row_modifiers["supplier"]))
    suppliers_button.place(relwidth=1, relheight=1/6, rely=2/6)
    allInv_button = tk.Button(selector_frame, text="All Inventory", command=lambda: products_query.run_and_display('Select * from allInventory', None, False, None, None))
    allInv_button.place(relwidth=1, relheight=1/6, rely=3/6)
    itemizedInv_button = tk.Button(selector_frame, text="Itemized Inventory", command=lambda: products_query.run_and_display('getEmployeeInventory', [None], False, insert_params["inventory"], row_modifiers["inventory"]))
    itemizedInv_button.place(relwidth=1, relheight=1/6, rely=4/6)
    usage_button = tk.Button(selector_frame, text="30 Day Usage", command=lambda: products_query.run_and_display('getProductsOverInterval', [30], False, None, None))
    usage_button.place(relwidth=1, relheight=1/6, rely=5/6)


def clients_menu():
    clear_widgets()
    title_text = tk.Label(root, text="Customers", font=('Helvetica', 12, 'bold'), bg=BG2_COLOR).place(relx=0.125, rely=0.17, relwidth=0.1, anchor='n')

    clients_query = query_display(root, cursor, "Select * from allCustomers", None, True, insert_params["customer"], row_modifiers["customer"])
    selector_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
    selector_frame.place(relx=0.125, rely=0.2, relwidth=0.1, relheight=0.6, anchor='n')
    home_button = tk.Button(selector_frame, text="Home", bg='#6666ff', command=lambda: main_menu())
    home_button.place(relwidth=1, relheight=1/6, rely=0)
    viewAll_button = tk.Button(selector_frame, text="All Customers", command=lambda: clients_query.run_and_display('Select * from allCustomers', None, True, insert_params["customer"], row_modifiers["customer"]))
    viewAll_button.place(relwidth=1, relheight=1/6, rely=2/6)
    viewAll_button = tk.Button(selector_frame, text="Unbilled", command=lambda: clients_query.run_and_display('Select * from unbilledClients', None, False, None, row_modifiers["unbilledCustomers"]))
    viewAll_button.place(relwidth=1, relheight=1/6, rely=3/6)
    viewAll_button = tk.Button(selector_frame, text="Overdue", command=lambda: clients_query.run_and_display('Select * from billingReminders', None, False, None, None))
    viewAll_button.place(relwidth=1, relheight=1/6, rely=4/6)
    viewAll_button = tk.Button(selector_frame, text="Lapsed", command=lambda: clients_query.run_and_display('Select * from appointmentReminders', None, False, None, None))
    viewAll_button.place(relwidth=1, relheight=1/6, rely=5/6)


def employees_menu():
    clear_widgets()
    title_text = tk.Label(root, text="Employees", font=('Helvetica', 12, 'bold'), bg=BG2_COLOR).place(relx=0.125, rely=0.17, relwidth=0.1, anchor='n')

    employees_query = query_display(root, cursor, "Select * from allEmployees", None, True, insert_params["employee"], row_modifiers["employee"])
    selector_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
    selector_frame.place(relx=0.125, rely=0.2, relwidth=0.1, relheight=0.6, anchor='n')
    home_button = tk.Button(selector_frame, text="Home", bg='#6666ff', command=lambda: main_menu())
    home_button.place(relwidth=1, relheight=1/6, rely=0)
    viewAll_button = tk.Button(selector_frame, text="View All", command=lambda: employees_query.run_and_display('Select * from allEmployees', None, True, insert_params["employee"], row_modifiers["employee"]))
    viewAll_button.place(relwidth=1, relheight=1/6, rely=2/6)
    viewCurrent_button = tk.Button(selector_frame, text="View Current", command=lambda: employees_query.run_and_display('Select * from currentEmployees', None, False, None, row_modifiers["employee"]))
    viewCurrent_button.place(relwidth=1, relheight=1/6, rely=3/6)


def invoice_menu():
    clear_widgets()
    title_text = tk.Label(root, text="Invoice", font=('Helvetica', 12, 'bold'), bg=BG2_COLOR).place(relx=0.125, rely=0.17, relwidth=0.1, anchor='n')

    invoice_query = query_display(root, cursor, "Select * from allCustomerInvoice", None, True, insert_params["customerInvoice"], row_modifiers["customer_invoice"])
    selector_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
    selector_frame.place(relx=0.125, rely=0.2, relwidth=0.1, relheight=0.6, anchor='n')
    home_button = tk.Button(selector_frame, text="Home", bg='#6666ff', command=lambda: main_menu())
    home_button.place(relwidth=1, relheight=1/6, rely=0)
    customer_button = tk.Button(selector_frame, text="Customer", command=lambda: invoice_query.run_and_display("Select * from allCustomerInvoice", None, True, insert_params["customerInvoice"], row_modifiers["customer_invoice"]))
    customer_button.place(relwidth=1, relheight=1/6, rely=2/6)
    supplier_button = tk.Button(selector_frame, text="Supplier", command=lambda: invoice_query.run_and_display("Select * from allSupplierInvoice", None, True, insert_params["supplierInvoice"], row_modifiers["supplier_invoice"]))
    supplier_button.place(relwidth=1, relheight=1/6, rely=3/6)
    payment_button = tk.Button(selector_frame, text="Payments", command=lambda: invoice_query.run_and_display("Select * from allPayments", None, True, insert_params["payment"], None))
    payment_button.place(relwidth=1, relheight=1/6, rely=4/6)


class query_display:
    def __init__(self, root, cursor, sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods):
        self.MAX_ROWS = 100
        global ENTRY_WIDTH
        self.search_entries = []
        self.sp_paramlist = sp_paramlist
        
        # query results frame
        self.query_display_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
        self.query_display_frame.place(relx=0.55, rely=0.2, relwidth=0.75, relheight=0.6, anchor='n')
        
        # refine search and insert frames
        self.refine_search_frame = None
        self.insert_frame = None

        self.run_and_display(sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods)
    
    def run_and_display(self, sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods):
        try:
            self.clear_display()
            self.sp_paramlist = sp_paramlist
            global col_headers
            global open_invoice
            open_invoice = None
            global last_ran_cmd_paramList
            last_ran_cmd_paramList = [sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods]

            # setup for scrollbar
            display_canvas = tk.Canvas(self.query_display_frame, highlightthickness=0)
            display_canvas.grid(row=0, column=0)
            scrollbar = tk.Scrollbar(self.query_display_frame, orient=tk.VERTICAL, command=display_canvas.yview)
            scrollbar.grid(row=0, column=1, sticky=tk.NSEW)
            display_canvas.configure(yscrollcommand=scrollbar.set)
            display_grid_frame = tk.Frame(display_canvas)
            
            if self.refine_search_frame:
                self.refine_search_frame.destroy()
                self.refine_search_frame = None
            if self.insert_frame:
                self.insert_frame.destroy()
                self.insert_frame = None
            
            response = []
            if sp_paramlist is None:
                # fetch full query results
                cursor.execute(sql_cmd)
                response = cursor.fetchall()
                col_headers = cursor.column_names
            else:
                # fetch stored procedure results
                cursor.callproc(sql_cmd, sp_paramlist)
                for result in cursor.stored_results():
                    response = result.fetchall()
                    col_headers = result.column_names

            num_rows = len(response) if len(response) < self.MAX_ROWS else self.MAX_ROWS
            #num_rows = len(response) if len(response) < 100 else 100
            num_columns = len(response[0])

            # update headers and entries
            for col in range(len(col_headers)):
                tk.Label(display_grid_frame, text=col_headers[col]).grid(row=0, column=col)

            # populate query results grid
            for row in range(num_rows):
                row_values = {}
                row_entries = {}
                for col in range(num_columns):
                    result_entry = tk.Entry(display_grid_frame, width=ENTRY_WIDTH)
                    result_entry.insert(0, (response[row][col] if response[row][col] else ""))
                    if row_mods:
                        if col in row_mods[0][3]:
                            result_entry.configure(state='disabled')
                    result_entry.grid(row=row+1, column=col)
                    row_values[col_headers[col]] = response[row][col]
                    row_entries[col_headers[col]] = result_entry
                if row_mods:
                    for mod_index in range(len(row_mods)):
                        if row_mods[mod_index][0] == "View":
                            insertKey = None
                            rowmodKey = None
                            if row_mods[mod_index][1] == "getCustomerInvoice":
                                insertKey = "customerInvoiceLine"
                                rowmodKey = "customer_invoice_line"
                            else:
                                insertKey = "supplierInvoiceLine"
                                rowmodKey = "supplier_invoice_line"
                            #print(insertKey, rowmodKey)
                            entry_mod_button = tk.Button(display_grid_frame, text=row_mods[mod_index][0], command=lambda sp_cmd = row_mods[mod_index][1], inv_id = response[row][0]: self.viewInvoice(inv_id, sp_cmd, [inv_id], False, insert_params[insertKey], row_modifiers[rowmodKey]))
                            entry_mod_button.grid(row=row+1, column=num_columns + mod_index)
                        else:
                            entry_mod_button = tk.Button(display_grid_frame, text=row_mods[mod_index][0], command=lambda modList = row_mods[mod_index], row_vals = row_entries: self.run_mod_and_refresh(modList, row_vals))
                            entry_mod_button.grid(row=row+1, column=num_columns + mod_index)

            # update scrollbar
            display_canvas.create_window((0,0), window=display_grid_frame, anchor=tk.NW)
            display_grid_frame.update_idletasks()
            bbox = display_canvas.bbox(tk.ALL)
            w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
            dw, dh = int(w), 430
            display_canvas.config(scrollregion=bbox, width=dw, height=dh)
        except:
            tk.Label(self.query_display_frame, text="No results", borderwidth=1).grid(row=0, column=0)
        
        if has_refine:
            self.refine_search_frame = refine_search_display(self)
        if insert_paramlist is not None:
            self.insert_frame = insert_display(insert_paramlist, self)
    
    def run_mod_and_refresh(self, modList, row_entries):
        params = []
        for entry in row_entries:
            if row_entries[entry].get():
                params.append(row_entries[entry].get())
            else:
                params.append(None)
        required_params = []
        for index in range(len(row_entries)):
            if index in modList[2]:
                required_params.append(params[index])
        #print(modList[1], required_params)
        cursor.callproc(modList[1], required_params)
        db_session.commit()
        global last_ran_cmd_paramList
        self.run_and_display(*last_ran_cmd_paramList)
    
    def clear_display(self):
        for widget in self.query_display_frame.winfo_children():
            widget.destroy()
        query_label = tk.Label(self.query_display_frame)
        query_label.place(relwidth=1, relheight=1)

        # clear other frames
        if self.refine_search_frame:
            self.refine_search_frame.clear_display()
        if self.insert_frame:
            self.insert_frame.clear_display()
    
    # hacky fix, time constraints
    def viewInvoice(self, invoice_num, sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods):
        self.run_and_display(sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods)
        global open_invoice
        open_invoice = invoice_num
        #print(invoice_num, sql_cmd, sp_paramlist, has_refine, insert_paramlist, row_mods)

class refine_search_display:
    def __init__(self, display_ref):
        self.search_entries = []
        self.display_ref = display_ref

        # search parameters
        self.search_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
        self.search_frame.place(relx=0.125, rely=0.05, relwidth=0.1, relheight=0.1, anchor='n')
        self.search_params_frame = tk.Frame(root, bg=BG_COLOR, bd=5)
        self.search_params_frame.place(relx=0.55, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')
        self.update_params_button = tk.Button(self.search_frame, text="Refine search", command=lambda: self.update_query())
        self.update_params_button.place(relheight=1, relwidth=1)
        
        self.update_params()

    def update_params(self):
        global col_headers
        global ENTRY_WIDTH

        for col in range(len(col_headers)):
            tk.Label(self.search_params_frame, text=col_headers[col], borderwidth=1, bg=BG_COLOR, font=('Helvetica', 10, 'bold')).grid(row=0, column=col)
            search_entry = tk.Entry(self.search_params_frame, width=ENTRY_WIDTH)
            search_entry.grid(row=1,column=col)
            self.search_entries.append(search_entry)
    
    def update_query(self):
        global last_ran_cmd_paramList
        global col_headers
        updated_param_list = last_ran_cmd_paramList[1:]
        updated_cmd = last_ran_cmd_paramList[0] + " WHERE "
        updated = False
        for entry in range(len(self.search_entries)):
            if self.search_entries[entry].get():
                updated_cmd += (cursor.column_names[entry] + self.search_entries[entry].get() + " AND ")
                updated = True
        if updated:
            updated_cmd = updated_cmd[:-5]
            updated_param_list.insert(0, updated_cmd)
            print(updated_param_list)
            self.display_ref.run_and_display(*updated_param_list)

    def clear_display(self):
        self.search_entries.clear()
        for widget in self.search_params_frame.winfo_children():
            widget.destroy()
        params_label = tk.Label(self.search_params_frame)
        params_label.place(relx=0, relwidth=1, relheight=1)

    def destroy(self):
        self.search_entries.clear()
        self.search_params_frame.destroy()
        self.search_frame.destroy()

class insert_display:
    def __init__(self, param_list, display_ref):
        self.insert_entries = []
        self.display_ref = display_ref

        # insert params
        self.insert_button_frame = tk.Frame(root, bg=BG_COLOR, bd=10)
        self.insert_button_frame.place(relx=0.125, rely=0.81, relwidth=0.1, relheight=0.12, anchor='n')
        self.insert_button = tk.Button(self.insert_button_frame, text="Add New", command=lambda: self.insert_entry(param_list))
        self.insert_button.place(relwidth=1, relheight=1)
        self.insert_params_frame = tk.Frame(root, bg=BG_COLOR, bd=5)
        self.insert_params_frame.place(relx=0.55, rely=0.81, relwidth=0.75, relheight=0.12, anchor='n')

        self.update_params(param_list)

    def update_params(self, param_list):
        global ENTRY_WIDTH
        self.sp_string = param_list[0]
        params = param_list[1:]

        for col in range(len(params)):
            tk.Label(self.insert_params_frame, text=params[col], borderwidth=1, bg=BG_COLOR, font=('Helvetica', 10, 'bold')).grid(row=0, column=col)
            insert_entry = tk.Entry(self.insert_params_frame, width=ENTRY_WIDTH)
            insert_entry.grid(row=1,column=col)
            self.insert_entries.append(insert_entry)
    
    # no easy refresh with this implementation
    def insert_entry(self, param_list):
        entry_values = []
        for entry in self.insert_entries:
            val = entry.get()
            if val:
                entry_values.append(val)
            else:
                entry_values.append(None)
        #ugly hax fix
        global open_invoice
        if open_invoice:
            entry_values.insert(0, open_invoice)
        global last_ran_cmd_paramList

        #print(param_list[0], entry_values)
        cursor.callproc(param_list[0], entry_values)
        db_session.commit()
        self.display_ref.run_and_display(*last_ran_cmd_paramList)

    
    def clear_display(self):
        self.insert_entries.clear()
        for widget in self.insert_params_frame.winfo_children():
            widget.destroy()
        insert_params_label = tk.Label(self.insert_params_frame)
        insert_params_label.place(relx=0, relwidth=1, relheight=1)

    def destroy(self):
        self.insert_entries.clear()
        self.insert_button_frame.destroy()
        self.insert_params_frame.destroy()


# START GUI
root = tk.Tk()
root.configure(background=BG2_COLOR)

# background
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg=BG2_COLOR, highlightthickness=0)
canvas.pack()

# load main menu
main_menu()

root.mainloop()
# END GUI

# cleanup
cursor.close()
db_session.close()