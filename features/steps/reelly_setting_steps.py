from behave import when, then
from time import sleep


@then('Click on Setting button')
def click_setting_btn(context):
    context.app.reelly_setting_page.click_setting_button()


@when('Click on User Guide button')
def click_user_guide_btn(context):
    context.app.reelly_setting_page.click_user_guide_btn()


@then('Verify that right page opens')
def verify_user_guide_page_opens(context):
    context.app.reelly_setting_page.verify_right_page()


@then('Verify all lesson videos contain title')
def verify_videos_contain_titles(context):
    context.app.reelly_setting_page.verify_video_title()