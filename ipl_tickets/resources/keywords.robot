*** Settings ***
Library    SeleniumLibrary    implicit_wait=0    run_on_failure=Nothing
Library    ../resources/BrowserSetup.py

*** Keywords ***
Open Browser With Saved Session
    Open Chrome Session
    Maximize Browser Window

Click When Available
    [Arguments]    ${locator}    ${timeout}=300
    [Documentation]    Polls and clicks the instant the element appears.
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
    Execute Javascript    document.querySelector("[aria-label='Book Tickets']").click()
