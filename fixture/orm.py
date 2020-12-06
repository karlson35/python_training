__author__ = 'Igor Nikolaev'
from pony.orm import *
from datetime import datetime

from model.contact import Contact
from model.group import Group


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        middlename = Optional(str, column='middlename')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str, column='title')
        address = Optional(str, column='address')
        tel_home = Optional(str, column='home')
        tel_mobile = Optional(str, column='mobile')
        tel_work = Optional(str, column='work')
        tel_fax = Optional(str, column='fax')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        bday = Optional(int, column='bday')
        bmonth = Optional(str, column='bmonth')
        byear = Optional(str, column='byear')
        aday = Optional(int, column='aday')
        amonth = Optional(str, column='amonth')
        ayear = Optional(str, column='ayear')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        notes = Optional(str, column='notes')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse="contacts",
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, autocommit=True)
        self.db.generate_mapping()
        sql_debug(True)

    @staticmethod
    def convert_groups_to_model(groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @staticmethod
    def convert_contacts_to_model(contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname,
                           middlename=contact.middlename, nickname=contact.nickname, company=contact.company,
                           title=contact.title, address=contact.address, tel_home=contact.tel_home,
                           tel_mobile=contact.tel_mobile, tel_work=contact.tel_work, tel_fax=contact.tel_fax,
                           email1=contact.email1,
                           email2=contact.email2, email3=contact.email3, homepage=contact.homepage, bday=contact.bday,
                           bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth,
                           ayear=contact.ayear, address2=contact.address2, phone2=contact.phone2, notes=contact.notes)
        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))