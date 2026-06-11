# Monthly Expenses Tracker 📊

A simple and interactive expense tracking web application built with **Streamlit**, **Pandas**, and **Plotly**. This application allows users to upload, manage, visualize, and download their monthly expense records.

## Features 🚀

* Upload an existing CSV file containing expense data.
* Add new expenses dynamically.
* Automatically update the cost of existing items.
* Visualize expenses using:

  * Bar Charts 📈
  * Pie Charts 🥧
* Download the updated expense data as a CSV file.
* Persistent data storage during the active Streamlit session using Session State.

---

## Technologies Used 🛠️

* Python
* Streamlit
* Pandas
* NumPy
* Plotly Express

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/monthly-expenses-tracker.git
cd monthly-expenses-tracker
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas numpy plotly
```

---

## Running the Application

Execute the following command in your terminal:

```bash
streamlit run app.py
```

Replace `app.py` with the name of your Python file if different.

---

## CSV File Format

The uploaded CSV file should follow this structure:

```csv
Things,Cost
Food,5000
Rent,12000
Internet,800
Transportation,2000
```

### Required Columns

| Column | Description      |
| ------ | ---------------- |
| Things | Expense Category |
| Cost   | Amount Spent     |

---

## How It Works

### Upload Expenses

Users can upload an existing CSV file containing expense records.

### Add New Expenses

* Enter the expense category in the **Things** field.
* Enter the amount in the **Cost** field.
* Click **Save Expenses**.

If the category already exists, the new cost is added to the existing amount.

### Visualize Data

Click:

* **Show Chart** → Displays a Bar Chart.
* **Pie Chart** → Displays a Pie Chart showing expense distribution.

### Download Updated Data

After making changes, click **Download Updated CSV** to save the latest expense data.

---

## Project Structure

```text
monthly-expenses-tracker/
│
├── app.py
├── README.md
├── requirements.txt
└── sample_expenses.csv
```

---

## Screenshots

You can add screenshots here after deploying the application:

```markdown
![Dashboard Screenshot](screenshots/dashboard.png)
```

---

## Future Improvements

* Monthly expense history tracking.
* Expense categorization.
* User authentication.
* Data persistence using SQLite or MySQL.
* Expense filtering and search functionality.
* Budget planning and alerts.

---

## Author

**Rudra Pratap Singh**

Aspiring AI Engineer | Python Developer | Data Analytics Enthusiast

GitHub: https://github.com/your-github-username

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project.
