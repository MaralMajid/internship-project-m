from behave import then



@then('Verify each product on this page contains a title and picture visible')
def pic_and_title_visible(context):
    context.app.reelly_pic_title_off_plan_page.pic_and_title_visible()