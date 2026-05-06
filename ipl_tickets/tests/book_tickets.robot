*** Settings ***
Resource    ../resources/keywords.robot

*** Variables ***
${MATCHURL}    https://www.district.in/events/tata-ipl-2026-match-49--sunrisers-hyderabad-vs-punjab-kings-buy-tickets

*** Test Cases ***
Auto Book IPL Ticket
    Open Browser With Saved Session
    Go To    ${MATCHURL}
    Click When Available    xpath=//button[@aria-label='Book Tickets']    timeout=600
