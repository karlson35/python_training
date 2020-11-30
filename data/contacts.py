__author__ = 'Igor Nikolaev'
from model.contact import Contact
import random
import string
import calendar


testdata = [Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                    title="title1", company="company1", address="address1",
                    tel_home="tel_home", tel_mobile="tel_mobile", tel_work="tel_work", tel_fax="tel_fax",
                    email1="email1", email2="email2", email3="email3", homepage="homepage",
                    bday="1", bmonth="-", byear="1988", aday="2", amonth="-", ayear="1998", group="[none]",
                    address2="address2",
                    phone2="phone2", notes="notes")]


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " " * 10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_tel(maxlen):
#     symbols = string.digits + "()- "
#     return "".join([random.choice(symbols) for i in range(maxlen)])
#
#
# testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
#                     tel_home="", tel_mobile="", tel_work="", tel_fax="", email1="", email2="", email3="", homepage="",
#                     bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", group="[none]", address2="",
#                     phone2="", notes="")] + [
#                Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#                        lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
#                        title=random_string("title", 10), company=random_string("company", 10),
#                        address=random_string("address", 10), tel_home=random_tel(10),
#                        tel_mobile=random_tel(10), tel_work=random_tel(10), tel_fax=random_tel(10),
#                        email1=random_string("email1", 10), email2=random_string("email2", 10),
#                        email3=random_string("email3", 10), homepage=random_string("homepage", 10),
#                        bday=str(random.randrange(31)), bmonth=random.choice(calendar.month_name[1:13]),
#                        byear=random.randrange(1900, 2020), aday=str(random.randrange(31)),
#                        amonth=random.choice(calendar.month_name[1:13]), ayear=random.randrange(1900, 2050),
#                        group="random", address2=random_string("address2", 10), phone2=random_tel(10),
#                        notes=random_string("notes", 10))
#                for i in range(5)
#            ]