## Overview

This project demonstrates a simple Django application with two models: `Customer` and `Order`. A customer can place multiple orders, and each order is associated with only one customer.

## Models

- **Customer**
  - `name`: A string field to store the customer's name.
  - `email`: An email field that must be unique for each customer.

- **Order**
  - `customer`: A foreign key linking to the `Customer` model, establishing a one-to-many relationship.
  - `order_date`: A date-time field that automatically sets to the current date and time when the order is created.
  - `total_amount`: A decimal field to store the total amount for the order.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django (install via `pip install django`)

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone <https://github.com/VictorMugoW/myproject>
   cd <myproject>

