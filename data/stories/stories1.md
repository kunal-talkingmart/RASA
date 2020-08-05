## Purchase
* browsecatalog
  - utter_letmesearchcategory
  - action_search_category
* inform{"category": "Gift Vouchers"}  
  - utter_letmesearchsubcategory
  - action_search_subcategory
* inform{"subcategory": "Gift Vouchers"} 
  - utter_askcity
* inform{"location": "Bangalore"}
  - utter_letmesearchproducts  
  - action_search_products
* tooexpensive
  - utter_letmesearchoptions
  - action_search_alternates
* addtocart ("product": "Buffet Experience At The Leela")
  - utter_addingtocart
  - action_addtocart  


## greet/bye path
* greet
  - utter_greet
  - utter_help

## say goodbye
* goodbye
  - utter_goodbye


## search transactions happy path
* greet
    - utter_greet
    - utter_help
* search_transactions
    - transact_search_form
    - form{"name": "transact_search_form"}
    - form{"name": null}
* thankyou
    - utter_noworries

## search transactions happy path no greet
* search_transactions
    - transact_search_form
    - form{"name": "transact_search_form"}
    - form{"name": null}
* thankyou
    - utter_noworries

## search transactions happy path no greet or thanks
* search_transactions OR check_earnings
    - transact_search_form
    - form{"name": "transact_search_form"}
    - form{"name": null}


## Show list of known recipients
* check_recipients
    - action_recipients

## Show credit accounts
* check_balance{"account_type":"credit"}
    - action_credit_card_balance

## Show specific credit account
* check_balance{"credit_card":"emblem"}
    - action_credit_card_balance

## Show credit accounts
* check_balance{"account_type":"credit","credit_card":"emblem"}
    - action_credit_card_balance

## story insult
* insult
    - utter_respond_insult
    - utter_help

## story telljoke
* telljoke
    - utter_telljoke
    - utter_help

## story ask_howdoing
* ask_howdoing
    - utter_askhowdoing
    - utter_help

## story ask_weather
* ask_weather
    - utter_ask_weather
    - utter_help

## story ask_builder
* ask_builder
    - utter_ask_builder
    - utter_help

## story ask_restaurant
* ask_restaurant
    - utter_ask_restaurant
    - utter_help

## story ask_wherefrom
* ask_wherefrom
    - utter_ask_wherefrom
    - utter_help

## story ask_time
* ask_time
    - utter_ask_time
    - utter_help

## story ask_howold
* ask_howold
    - utter_ask_howold
    - utter_help

## story ask_whoami
* ask_whoami
    - utter_ask_whoami
    - utter_help

## story ask_languagebot
* ask_languagebot
    - utter_ask_languagebot
    - utter_help

## story ask_whatismyname
* ask_whatismyname
    - utter_ask_whatismyname
    - utter_help

## help
* help
    - utter_help