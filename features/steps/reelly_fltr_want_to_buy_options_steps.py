from behave import when, then
from time import sleep



@then('Click on "Secondary" option at the left side menu')
def click_on_secondary_option_menu(context):
    context.app.reelly_fltr_want_to_buy_page.click_on_secondary_option_menu()



@when('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.reelly_fltr_want_to_buy_page.verify_right_page_opens()



@then('Click on Filters')
def click_on_filters(context):
    context.app.reelly_fltr_want_to_buy_page.click_on_filters()



@then('Filter the products by "Want to buy"')
def select_want_yo_buy(context):
    context.app.reelly_fltr_want_to_buy_page.select_want_to_buy()



@then('Click on Apply Filter')
def click_on_apply_filter(context):
    context.app.reelly_fltr_want_to_buy_page.click_apply_filter()



@then('Verify all cards have "want to buy" tag')
def verify_all_card_tags(context):
    context.app.reelly_fltr_want_to_buy_page.all_card_tags()