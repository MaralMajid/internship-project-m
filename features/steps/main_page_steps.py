from behave import then



@then('Verify that main page')
def verify_text_total_project(context):
    context.app.main_page.verify_msg()