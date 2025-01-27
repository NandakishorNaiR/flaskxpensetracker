# Flask Expense Tracker Documentation

## **Overview**

The Flask Expense Tracker is a simple web application that helps users track daily expenses across different categories such as "Food," "Transport," "Entertainment," and "Others." The application allows users to dynamically add expenses and view a summary of total expenses and category-wise spending percentages.

---

## **Features**

1. Add expenses dynamically.
2. Categorize expenses (Food, Transport, Entertainment, Others).
3. View a summary of total expenses.
4. Display percentage-wise distribution of expenses across categories.
5. Responsive and styled using basic HTML and CSS.

---

## **Project Structure**

```
mydynamicExpenseTracker/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── .gitignore
```

### **Key Files**

1. **app.py**: The core Flask application file that handles routes, logic, and server operations.
2. **templates/index.html**: The HTML file that defines the structure and layout of the web interface.
3. **static/style.css**: The CSS file that provides styling for the application.
4. **requirements.txt**: Contains the Python dependencies needed to run the application.
5. **.gitignore**: Specifies files and directories to be ignored by Git (e.g., virtual environment files, caches).

---

## **Setup Instructions**

### **Prerequisites**

- Python 3.8 or higher
- pip (Python package manager)
- Git

### **Steps to Run Locally**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd mydynamicExpenseTracker
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Linux/Mac
   .\env\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   python app.py
   ```

5. **Access the Application**:
   Open a web browser and navigate to:

   ```
   http://127.0.0.1:5000
   ```

---

## **Usage**

1. **Adding Expenses**:

   - Select a category from the dropdown menu.
   - Enter the expense amount in the input box.
   - Click the "Add Expense" button.

2. **Viewing Summary**:

   - The summary section displays the total expenses and a breakdown of expenses by category with their respective percentages.

---

## **Key Routes**

### **`/`**\*\* (Home Route)\*\*

- **Methods**: `GET`, `POST`
- **Description**: Handles the main functionality of the application.
  - On `POST`: Adds a new expense to the selected category.
  - On `GET`: Displays the current summary of expenses.

---

## **Example Data Flow**

1. User submits an expense (e.g., \$20 for Food).
2. The form sends a `POST` request to the `/` route.
3. The server updates the `expenses` dictionary and recalculates the totals and percentages.
4. The updated summary is rendered on the page via `index.html`.

---

## **Code Explanation**

### **app.py**

- Initializes Flask application.
- Defines categories and maintains an `expenses` dictionary to track amounts.
- Handles routes for adding expenses and displaying the summary.

### **templates/index.html**

- Provides a user-friendly interface for interacting with the application.
- Displays the form for adding expenses and a table for the expense summary.

### **static/style.css**

- Enhances the visual appeal of the application with styling for form elements, buttons, and tables.

---

## **Deployment**

### **Steps to Deploy on Render**

1. Push the project to GitHub.
2. Log in to [Render](https://render.com/).
3. Create a new Web Service and link it to your GitHub repository.
4. Set the `Start Command` to:
   ```bash
   gunicorn app:app
   ```
5. Specify the environment (Python version, dependencies, etc.).
6. Deploy the application.
7. Access the deployed app using the provided URL.

---

## **Future Improvements**

1. Add user authentication to track expenses for multiple users.
2. Include a date filter to view expenses for specific time periods.
3. Implement a graphical representation (e.g., pie chart) for expense summaries.
4. Add a database (e.g., SQLite, PostgreSQL) for persistent data storage.

---

## **Credits**

Developed by -Nandakishore Sasi Nair.

