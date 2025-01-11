from behave import when, then


@then('Click on Sales status')
def click_on_sale_status(context):
    context.app.reelly_out_of_stock_fltr_page.click_on_sale_status()



@then('Filter by sale status of “Out of Stocks”')
def filter_by_sale_status(context):
    context.app.reelly_out_of_stock_fltr_page.click_on_out_of_stock()


@then('Verify each product contains the Out of Stocks tag')
def verify_tags(context):
    context.app.reelly_out_of_stock_fltr_page.verify_tags()