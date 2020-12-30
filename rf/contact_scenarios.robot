*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname_robot  lastname_robot
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    rf.AddressBook.Contact Lists Should Be Equal  ${old_list}  ${new_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New Contact  firstname_robot_modified  lastname_robot_modified
    Modify Contact  ${new_contact}  ${contact}
    ${new_list}=  Get Contact List
    Set List Value  ${old_list}  ${index}  ${new_contact}
    rf.AddressBook.Contact Lists Should Be Equal  ${old_list}  ${new_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    rf.AddressBook.Contact Lists Should Be Equal  ${old_list}  ${new_list}