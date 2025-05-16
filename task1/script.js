// Expense class to represent each expense
class Expense {
    constructor(category, amount) {
        this.id = Date.now();
        this.category = category;
        this.amount = parseFloat(amount);
        this.date = new Date();
    }
}

// ExpenseManager class to handle all expense-related operations
class ExpenseManager {
    constructor() {
        this.expenses = this.loadExpenses();
        this.form = document.getElementById('expenseForm');
        this.tableBody = document.getElementById('expensesTableBody');
        this.totalExpensesElement = document.getElementById('totalExpenses');
        this.dailyAverageElement = document.getElementById('dailyAverage');
        this.topExpensesElement = document.getElementById('topExpenses');

        this.initializeEventListeners();
        this.updateDisplay();
    }

    // Load expenses from localStorage
    loadExpenses() {
        const savedExpenses = localStorage.getItem('expenses');
        return savedExpenses ? JSON.parse(savedExpenses) : [];
    }

    // Save expenses to localStorage
    saveExpenses() {
        localStorage.setItem('expenses', JSON.stringify(this.expenses));
    }

    // Initialize event listeners
    initializeEventListeners() {
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.addExpense();
        });
    }

    // Add new expense
    addExpense() {
        const category = document.getElementById('category').value.trim();
        const amount = document.getElementById('amount').value;

        if (!category || !amount) {
            alert('Please fill in all fields');
            return;
        }

        const expense = new Expense(category, amount);
        this.expenses.push(expense);
        this.saveExpenses();
        this.updateDisplay();
        this.form.reset();
    }

    // Delete expense
    deleteExpense(id) {
        this.expenses = this.expenses.filter(expense => expense.id !== id);
        this.saveExpenses();
        this.updateDisplay();
    }

    // Calculate total expenses
    calculateTotal() {
        return this.expenses.reduce((sum, expense) => sum + expense.amount, 0);
    }

    // Calculate daily average
    calculateDailyAverage() {
        return this.calculateTotal() / 30;
    }

    // Get top 3 expenses
    getTopExpenses() {
        return [...this.expenses]
            .sort((a, b) => b.amount - a.amount)
            .slice(0, 3);
    }

    // Format currency
    formatCurrency(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(amount);
    }

    // Format date
    formatDate(date) {
        return new Date(date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    }

    // Update the display
    updateDisplay() {
        // Update table
        this.tableBody.innerHTML = '';
        this.expenses.forEach(expense => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${expense.category}</td>
                <td>${this.formatCurrency(expense.amount)}</td>
                <td>${this.formatDate(expense.date)}</td>
                <td>
                    <button class="btn btn-danger btn-sm" onclick="expenseManager.deleteExpense(${expense.id})">
                        Delete
                    </button>
                </td>
            `;
            this.tableBody.appendChild(row);
        });

        // Update totals
        this.totalExpensesElement.textContent = this.formatCurrency(this.calculateTotal());
        this.dailyAverageElement.textContent = this.formatCurrency(this.calculateDailyAverage());

        // Update top 3 expenses
        const topExpenses = this.getTopExpenses();
        this.topExpensesElement.innerHTML = '';
        if (topExpenses.length === 0) {
            this.topExpensesElement.innerHTML = '<li class="list-group-item">No expenses yet</li>';
        } else {
            topExpenses.forEach(expense => {
                const li = document.createElement('li');
                li.className = 'list-group-item';
                li.textContent = `${expense.category}: ${this.formatCurrency(expense.amount)}`;
                this.topExpensesElement.appendChild(li);
            });
        }
    }
}

// Initialize the expense manager
const expenseManager = new ExpenseManager(); 