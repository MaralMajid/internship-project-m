from behave import given, when, then


@given ('Open Reelly url')
def open_url(context):
    context.app.web_app_page.open()


@when ('Click on Sign in button')
def click_sign_in_button(context):
    context.app.web_app_page.click()


@when('Input correct email address')
def input_email(context):
    context.app.sign_in_page.input_email()



@when('Input correct password')
def input_password(context):
    context.app.sign_in_page.input_password()



@then('Click on continue button')
def click_continue_button(context):
    context.app.sign_in_page.click()