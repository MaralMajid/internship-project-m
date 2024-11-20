from behave import when, then
from time import sleep


@then('Click on "Off-plan" option at the left side menu')
def click_off_plan(context):
    context.app.reelly_off_plan_price_page.click_off_plan()


@when('Verify the right page open')
def verify_right_page(context):
    context.app.reelly_off_plan_price_page.verify_right_url()


@then('Click on Filter')
def click_filter(context):
    context.app.reelly_off_plan_price_page.click_on_filter()