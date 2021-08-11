# The Setup

1. Create a virtual environment, python 3.6+.
2. Install dependencies mentioned in requirements.txt file
3. To check if its working run :
 	=> python manage.py runserver
4. To apply in-built migrations:
	=> python manage.py migrate
5. To populate masters, run:
	=> python manage.py populate_masters


# WORK

**Objective:**

APIs for a transaction.

**APIs endpoint**

1.  Add a transaction document with its line items.
    
2.  Add line items once a transaction is created.
    
3.  Add multiple inventory items to line items.
    
4.  Delete a transaction, cant be deleted if inventory is created.
    
5.  View a transaction with all its line items and their inventory items.
