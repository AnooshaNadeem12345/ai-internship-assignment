# ai-internship-assignment

Name: Anoosha Nadeem
Assignment Title : AI Internship Assignment – 1:  Desi Restaurant System
Description:# 🍽️ Desi Restaurant Management System

A simple Python console application that simulates an order management system for a desi (South Asian) restaurant. Built using core programming fundamentals — **functions, loops, and if-else conditionals** — to handle customer orders for Karahi, Biryani, BBQ, and Chai.

## 📋 Features

- Takes orders from **5 customers** in a loop
- Supports four menu items: `karahi`, `biryani`, `bbq`, `chai`
- Asks follow-up questions based on the item ordered:
  - **Karahi** → asks for spice level (`high` / `medium` / `low`)
  - **BBQ** → asks for number of pieces
  - **Chai** → asks for sugar level (`high` / `medium` / `low`)
  - **Biryani** → no follow-up needed, served directly
- Returns a friendly, descriptive message for each order
- Handles invalid items gracefully with an "Item not available ❌" message

## 🛠️ Built With

- Python 3
- Functions (`def`)
- Conditional statements (`if` / `elif` / `else`)
- Loops (`for`)
- `input()` and `return` for interactive, reusable logic

## 🚀 How to Run

1. Make sure Python is installed on your system. Check with:
   ```bash
   python --version
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/desi-restaurant-management-system.git
   cd desi-restaurant-management-system
   ```
3. Run the script:
   ```bash
   python restaurant.py
   ```
4. Follow the prompts to place orders for 5 customers.

## 📷 Example Output

```
Customer 1 → Enter item (karahi/biryani/bbq/chai): biryani
Customer 1 → biryani → Biryani is ready

Customer 2 → Enter item (karahi/biryani/bbq/chai): chai
Enter sugar level (high, medium, low): high
Customer 2 → chai → Sweet Chai

Customer 3 → Enter item (karahi/biryani/bbq/chai): karahi
Enter spice level (high, medium, low): high
Customer 3 → karahi → Spicy Karahi

Customer 4 → Enter item (karahi/biryani/bbq/chai): bbq
Enter number of BBQ pieces: 7
Customer 4 → bbq → Half BBQ Platter

Customer 5 → Enter item (karahi/biryani/bbq/chai): burger
Customer 5 → burger → Item not available ❌
```

## 📂 Project Structure

```
desi-restaurant-management-system/
│
├── restaurant.py     # Main Python script
└── README.md         # Project documentation
```

## 🎯 Learning Objectives

This project was built as a practice exercise to strengthen understanding of:
- Writing and calling functions with parameters and return values
- Using `if-elif-else` chains for decision-making
- Looping through repeated tasks (multiple customers)
- Structuring a small, real-world-style console application

## 📜 License

This project is open-source and free to use for learning purposes.
