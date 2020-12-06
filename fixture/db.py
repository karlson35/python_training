__author__ = 'Igor Nikolaev'

import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, middlename, nickname, company, title, address, home, "
                           "mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, "
                           "ayear, address2, phone2, notes from addressbook")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, company, title, address, home,
                 mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth,
                 ayear, address2, phone2, notes) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                            nickname=nickname, company=company, title=title, address=address,
                                            tel_home=home, tel_mobile=mobile, tel_work=work, tel_fax=fax, email1=email,
                                            email2=email2, email3=email3, homepage=homepage, bday=bday, bmonth=bmonth,
                                            byear=byear, aday=aday, amonth=amonth, ayear=ayear, address2=address2,
                                            phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
