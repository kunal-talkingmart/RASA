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
* addtocart ("product": "Buffet Experience At The Leela")
  - utter_addingtocart
  - action_addtocart  
* showcart
  - action_showcart  
  


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
## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform{"category": "Vouchers"}
    - slot{"category": "Vouchers"}
    - action_search_subcategory
* inform{"subcategory": "deals"}
    - slot{"subcategory": "deals"}
    - utter_askcity
* inform{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_letmesearchproducts
    - action_search_products
* addtocart{"product": "practo online"}
    - slot{"product": "practo online"}
    - action_addtocart
* showcart
    - action_showcart

## interactive_story_1
* greet
    - utter_greet
    - utter_help
* inform{"category": "Vouchers"}
    - slot{"category": "Vouchers"}
    - action_search_subcategory
* inform{"subcategory": "beauty"}
    - slot{"subcategory": "beauty"}
    - utter_askcity
* inform{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_letmesearchproducts
    - action_search_products
* addtocart{"product": "netmeds"}
    - slot{"product": "netmeds"}
    - action_addtocart
* showcart
    - action_showcart
* inform{"category": "Vouchers"}
    - slot{"category": "Vouchers"}
    - utter_letmesearchsubcategory
    - action_search_subcategory
* inform{"subcategory": "apparel"}
    - slot{"subcategory": "apparel"}
    - utter_askcity
* inform{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_letmesearchproducts
    - action_search_products
* addtocart{"product": "shoppers stop"}
    - slot{"product": "shoppers stop"}
    - action_addtocart
* showcart
    - action_showcart
* inform{"category": "Vouchers"}
    - slot{"category": "Vouchers"}
    - utter_letmesearchsubcategory
    - action_search_subcategory
* inform{"subcategory": "music"}
    - slot{"subcategory": "music"}
    - utter_askcity
* inform{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_letmesearchproducts
    - action_search_products
* addtocart{"product": "Saregama Carvaan"}
    - slot{"product": "Saregama Carvaan"}
    - action_addtocart
* showcart
    - action_showcart
* inform{"category": "experiences"}
    - slot{"category": "experiences"}
    - action_search_subcategory
* inform{"subcategory": "hobbies"}
    - slot{"subcategory": "hobbies"}
    - utter_askcity
* inform{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_letmesearchproducts
    - action_search_products
* addtocart{"product": "escape the tomb"}
    - slot{"product": "escape the tomb"}
    - action_addtocart
* showcart
    - action_showcart

