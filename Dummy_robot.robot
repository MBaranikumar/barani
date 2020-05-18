
*** Test Cases ***
For Test
    [Tags]    test-tag
    : FOR    ${i}    IN RANGE    0    10
    \    Log    ${i}
    Log    Exited

PRINT_CMD_IN_LOG
    [Documentation]    My First App
    Log To Console    Hi Guys
    Log    Hello All
