# Expense Tracker
# Proyecto para practicar lógica básica, listas y funciones

expenses = []

def add_expense(description, amount):
    """Agrega un gasto a la lista"""
    expenses.append({
        "description": description,
        "amount": amount
    })

def show_expenses():
    """Muestra los gastos y el total"""
    total = 0
    for expense in expenses:
        print(f"- {expense['description']}: ${expense['amount']}")
        total += expense['amount']
    print(f"Total gastado: ${total}")

add_expense("Comida", 5000)
add_expense("Transporte", 2000)
show_expenses()
