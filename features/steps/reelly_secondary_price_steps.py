from behave import when, then
from time import sleep


@then('Filter the products by price range from 1200000 AED')
def price_input_from(context):
    context.app.reelly_secondary_price_page.price_filter_from()


@then('Filter the products by price range to 2000000 AED')
def price_input_to(context):
    context.app.reelly_secondary_price_page.price_filter_to()



@then('Verify the price in all cards inside the range')
def price_inside_range(context):
    context.app.reelly_secondary_price_page.verify_price_range()