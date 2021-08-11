## Transaction Endpoints
### Endpoints Description
    ` There are 5 transaction endpoints (as of now)  'trn/', 'trnitem/', 'invent/', 'trnview/', 'trndel/' `

- The ```trn/``` endpoint takes *[company, branch, department, remarks(optional)]* fields in POST request to create a new transaction. It return the *transaction_id, transaction_number, company, branch, department*
- The ```trnitem/``` endpoint takes *[transaction_number, article, colour, required_date(yyyy-mm-dd), qty, rate, unit (KG/M)]* fields in POST request to add the item line. The transaction_number is a field which tells us the transaction to which item-line belong to. It returns the *trn_item_id, trn_item_article, trn_item_colour*
- The ```invent/``` endpoint takes *[transaction_item_id, article, colour, company, gross_qty, net_qty, unit(KG/M)]* fields in POST request to add the product data in inventory table. The transaction_item_id is a field which tells us the transaction_item_line to which product belongs to It returns the *invent_id, invent_article, invent_colour, invent_company*
- The ```trnview/``` endpoint takes *[transaction_number]* fields in POST request to show the details of that particular transaction. It returns transaction details in nested line-items related to that particular transaction_number.
- The ```trndel/``` endpoint takes *[transaction_number]* fields in POST request to delete that particular transaction.

### Assumptions and Cases
- Cases:
  - It is a backend code, which needs to be tested using 'request library' or 'postman'.

- Assumptions:
  - company tag only accept one of following ['Ace']
  - branch tag only accept one of the following ['SUN', 'MOON']
  - department tag only accept one of following ['Warp Knitting','DPV']
  - article tag only accept one of following ['YarnArticle1', 'YarnArticle2']
  - colour tag only accept one of following ['White', 'Black', 'Red', 'Green', 'Yellow', 'Orange', 'Blue']
  - unit tag only accept one of following ['KG', 'M']
  
Regards: Himanshu Khairajani