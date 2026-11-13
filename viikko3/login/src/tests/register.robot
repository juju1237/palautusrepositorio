*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register User  matti  salasana
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register User  ab  salasana
    Register Should Fail

Register With Valid Username And Too Short Password
    Register User  matti  salasan
    Register Should Fail

Register With Username That Is Already In Use
    Register User  kalle  salasana
    Register Should Fail

*** Keywords ***
Register User
    [Arguments]  ${username}  ${password}
    Fill Text  id=username  ${username}
    Fill Secret  id=password  $password
    Fill Secret  id=password_confirmation  $password
    Click  button >> text=Register

Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail
    Register Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
