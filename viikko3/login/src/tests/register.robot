*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Matching Password And Confirmation
    Register User  matti  salasana1  salasana1
    Register Should Succeed

Register With Different Password And Confirmation
    Register User  matti  salasana1  salasana2
    Register Should Fail With Error

Register With Valid Username And Password
    Register User  matti  salasana1
    Register Should Succeed

Register With Password Containing Numbers
    Register User  matti  kalle123
    Register Should Succeed

Register With Password Containing Special Character
    Register User  matti  kalle#abc
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

Register With Password Containing Only Lowercase Letters
    Register User  matti  kallekalle
    Register Should Fail With Error

Register With Password Containing Only Uppercase And Lowercase Letters
    Register User  matti  KalleKalle
    Register Should Fail With Error

*** Keywords ***
Register User
    [Arguments]  ${username}  ${password}  ${password_confirmation}=${password}
    Fill Text  id=username  ${username}
    Fill Secret  id=password  $password
    Fill Secret  id=password_confirmation  $password_confirmation
    Click  button >> text=Register

Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail
    Register Page Should Be Open

Register Should Fail With Error
    Register Page Should Be Open
    Get Text  css=ul li  !=  ${EMPTY}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To  ${REGISTER_URL}
