import pickle

class Customer:
    def __init__(self, customer_id, name, email, password, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def __str__(self):
        return f"{self.name} ({self.email})"

# Customer list
customers = [
    Customer(1, "Amna Ibrahim", "amna@gmail.com", "amna123", "1234567890"),
    Customer(2, "Almaha Ibrahim", "almaha@gmail.com", "almaha123", "0987654321"),
    Customer(3, "Salem Saeed", "salem@gmail.com", "salem123", "1122334455"),
    Customer(4, "Shaikha Saleh", "shaikha@gmail.com", "shaikha123", "6677889910"),
    Customer(5, "Afshan Parker", "afshan@gmail.com", "afshan123", "5544332211"),
]

# Ticket sales summary
tickets_sold = {
    "2025-05-04": 10,
    "2025-05-03": 5
}

# Full purchase history
purchase_history = [
    {"customer_id": 1, "ticket_type": "Weekend Package", "purchase_time": "2025-05-03 14:30"},
    {"customer_id": 2, "ticket_type": "Single Race Pass", "purchase_time": "2025-05-04 16:45"},
    {"customer_id": 3, "ticket_type": "Group Discount", "purchase_time": "2025-05-04 12:00"},
    {"customer_id": 4, "ticket_type": "Weekend Package", "purchase_time": "2025-05-02 15:10"},
    {"customer_id": 5, "ticket_type": "Single Race Pass", "purchase_time": "2025-05-01 18:20"}
]

discount_enabled = True

tickets = [
    {
        "type": "Single Race Pass",
        "price": 100,
        "validity": "1 day",
        "features": "Access to 1 race"
    },
    {
        "type": "Weekend Package",
        "price": 250,
        "validity": "3 days",
        "features": "All races + pit tour"
    },
    {
        "type": "Group Discount",
        "price": 80,
        "validity": "1 day",
        "features": "Minimum 5 people"
    }
]

admin_credentials = {
    "admin": "admin123"
}

# Save all data
data = {
    "customers": customers,
    "tickets_sold": tickets_sold,
    "discount_enabled": discount_enabled,
    "tickets": tickets,
    "admin_credentials": admin_credentials,
    "purchase_history": purchase_history
}

with open("ticket_data.pickle", "wb") as f:
    pickle.dump(data, f)
