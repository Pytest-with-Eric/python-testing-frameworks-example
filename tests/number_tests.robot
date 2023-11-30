*** Settings ***
Library     ../src/check_number.py

*** Test Cases ***
Test Negative Number
    ${result}=    check_number    -2
    Should Be Equal As Strings    ${result}    Negative

Test Zero
    ${result}=    check_number    0
    Should Be Equal As Strings    ${result}    Zero

Test Positive Number
    ${result}=    check_number    3
    Should Be Equal As Strings    ${result}    Positive
