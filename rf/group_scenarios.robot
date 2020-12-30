*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    APPEND TO LIST  ${old_list}  ${group}
    rf.AddressBook.Group Lists Should Be Equal  ${old_list}  ${new_list}


Delete Group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get from list  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    REMOVE VALUES FROM LIST  ${old_list}  ${group}
    rf.AddressBook.Group Lists Should Be Equal  ${old_list}  ${new_list}
