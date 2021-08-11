## Transaction Endpoints
### Endpoints Description
    There are 5 seller endpoints (as of now)  `trn/,trnitem/,invent/,trnview/,trndel/`.

- The ```trn/``` endpoint takes *[company, branch, department, remarks(optional)]* fields in POST request to create a new transaction. It return the *transaction_id, transaction_number*
- The ```trnitem/``` endpoint takes *[transaction_number, article, colour, required_date(yyyy-mm-dd) qty, rate, unit (Kg/M)]* fields in POST request to add the item line. The transaction_number is a field which tells us the transaction to which item-line belong to. It returns the *trn_item_id, trn_item_article*
- The ```invent/``` endpoint takes *[transaction_item_id,article,colour,company,gross_qty,net_qty, unit(Kg/M]* fields in POST request to add the product data in inventory table. The transaction_item_id is a field which tells us the transaction_item_line to which product belongs to It returns the *invent_id, invent_article*
- The ```trnview/``` endpoint takes *[transaction_number]* fields in POST request to show the details of that particular transaction.
- The ```trndel/``` endpoint takes *[transaction_number]* fields in POST request to delete that particular transaction.


Regards: Himanshu Khairajani