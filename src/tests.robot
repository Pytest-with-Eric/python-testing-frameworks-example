*** Settings ***
Library    ../src/check_number.py

*** Test Cases ***
Testing check_number function
    Log To Console    Starting test
    Verify app calculation    -2    Negative

*** Keywords ***
Verify app calculation 
    [Arguments]    ${term}    ${expected}
    Log To Console    Calculating: ${term}
    ${actual}    check_number    ${term}
    Log To Console    Calculated Result: ${actual}
    Should Be Equal As Numbers    ${actual}    ${expected}