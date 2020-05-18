*** Settings ***
Library  C:/barani_repo/barani/barani/rep_word.py

*** Variables ***

*** Keywords ***
repeat word count
    ${g}=  rep_word
    log  ${g}

*** Test Cases ***
verify the count of repated word
    [Tags]    trail
    repeat word count