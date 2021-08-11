## Transaction Endpoints
### Endpoints Description
    ` There are 5 transaction endpoints (as of now)  'trn/', 'trnitem/', 'invent/', 'trnview/', 'trndel/' `

- The ```http://127.0.0.1:8869/trn/``` endpoint takes *[company, branch, department, remarks(optional)]* fields in POST request to create a new transaction. It return the *transaction_id, transaction_number, company, branch, department*
- The ```http://127.0.0.1:8869/trnitem/``` endpoint takes *[transaction_number, article, colour, required_date(yyyy-mm-dd), qty, rate, unit (KG/M)]* fields in POST request to add the item line. The transaction_number is a field which tells us the transaction to which item-line belong to. It returns the *trn_item_id, trn_item_article, trn_item_colour*
- The ```http://127.0.0.1:8869/invent/``` endpoint takes *[transaction_item_id, article, colour, company, gross_qty, net_qty, unit(KG/M)]* fields in POST request to add the product data in inventory table. The transaction_item_id is a field which tells us the transaction_item_line to which product belongs to It returns the *invent_id, invent_article, invent_colour, invent_company*
- The ```http://127.0.0.1:8869/trnview/``` endpoint takes *[transaction_number]* fields in POST request to show the details of that particular transaction. It returns transaction details in nested line-items related to that particular transaction_number.
- The ```http://127.0.0.1:8869/trndel/``` endpoint takes *[transaction_number]* fields in POST request to delete that particular transaction.

### Doubts
- If we have multiple inventory items linked to individual list-item, then why instead of having foreign-key as inventory-id, we having field such as 'article' and 'colour' in list-item table ? 
- Ideally i guess rate should be the field of inventory-item and not list-item. 
- Also, the qty will be the total of all the inventory items linked to a particular list item, right ?

### Assumptions and Cases
- Cases:
  - company tag only accept one of following ['Ace']
  - branch tag only accept one of the following ['SUN', 'MOON']
  - department tag only accept one of following ['Warp Knitting','DPV']
  - article tag only accept one of following ['YarnArticle1', 'YarnArticle2']
  - colour tag only accept one of following ['White', 'Black', 'Red', 'Green', 'Yellow', 'Orange', 'Blue']
  - unit tag only accept one of following ['KG', 'M']

- Assumptions:
  - It is a backend code, which needs to be tested using 'request library' or 'postman'.
  - There is a list-item table, which is having all the inputs as mentioned, along with article, colour etc. 
  - Inventory is having foreign key as list-item. (ideally it should be opposite as per my doubts)


  
Regards: Himanshu Khairajani