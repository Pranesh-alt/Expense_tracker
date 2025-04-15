document.addEventListener("DOMContentLoaded", () => {
    const expenseList = document.getElementById("expense-list");
    const totalExpense = document.getElementById("total-expense");
    const categorySelect = document.getElementById("category");
    const transactionTypeSelect = document.getElementById("transaction-type");
    const ctx = document.getElementById("expenseChart").getContext("2d");

    let expenses = [];
    let expenseChart;

    async function fetchExpenses() {
        try {
            const response = await fetch("/");
            expenses = await response.json();
            updateExpenseList();
            updateChart();
            updateTotal();
        } catch (error) {
            console.error("Error fetching expenses:", error);
        }
    }

    function updateTotal() {
        const total = expenses.reduce((sum, exp) => exp.transaction.toLowerCase() === "expense" ? sum - exp.amount : sum + exp.amount, 0);
        totalExpense.textContent = `$${total.toFixed(2)}`;
    }

    function updateExpenseList() {
        expenseList.innerHTML = "";
        expenses.forEach(expense => {
            const li = document.createElement("li");
            li.textContent = `${expense.transaction.toUpperCase()} - ${expense.category}: $${expense.amount.toFixed(2)}`;
            expenseList.appendChild(li);
        });
    }

    function updateChart() {
        if (!expenses.length) {
            console.log("No expenses found, skipping chart update.");
            return;
        }
    
        const categories = [...new Set(expenses.map(exp => exp.category))];
        const categoryTotals = categories.map(cat => 
            expenses.filter(exp => exp.category === cat).reduce((sum, exp) => sum + exp.amount, 0)
        );
    
        if (expenseChart) {
            expenseChart.destroy();
        }
    
        expenseChart = new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: categories,
                datasets: [{
                    label: "Expenses by Category",
                    data: categoryTotals,
                    backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"],
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
    
    async function addExpense() {
        const amount = parseFloat(prompt("Enter amount:"));
        if (isNaN(amount) || amount <= 0) {
            alert("Please enter a valid amount.");
            return;
        }

        const category = categorySelect.value;
        const transaction = transactionTypeSelect.value;
        
        const newExpense = { amount, category, transaction };
        
        try {
            await fetch("http://127.0.0.1:8001/expenses", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(newExpense)
            });
            await fetchExpenses();
        } catch (error) {
            console.error("Error adding expense:", error);
        }
    }

    window.addExpense = addExpense;
    fetchExpenses();
});