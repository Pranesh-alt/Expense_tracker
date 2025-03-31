document.addEventListener("DOMContentLoaded", () => {
    const expenseList = document.getElementById("expense-list");
    const totalExpense = document.getElementById("total-expense");
    const categorySelect = document.getElementById("category");
    const transactionTypeSelect = document.getElementById("transaction-type");

    let expenses = [];

    function updateTotal() {
        const total = expenses.reduce((sum, exp) => exp.type === "expense" ? sum - exp.amount : sum + exp.amount, 0);
        totalExpense.textContent = `$${total.toFixed(2)}`;
    }

    function addExpense() {
        const amount = parseFloat(prompt("Enter amount:"));
        if (isNaN(amount) || amount <= 0) {
            alert("Please enter a valid amount.");
            return;
        }

        const category = categorySelect.value;
        const type = transactionTypeSelect.value;
        
        const expense = { amount, category, type };
        expenses.push(expense);

        const li = document.createElement("li");
        li.textContent = `${type.toUpperCase()} - ${category}: $${amount.toFixed(2)}`;
        expenseList.appendChild(li);

        updateTotal();
    }

    window.addExpense = addExpense;
});
