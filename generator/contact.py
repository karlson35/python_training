from model.contact import Contact
import random
import string
import calendar
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_tel(maxlen):
    symbols = string.digits + "()- "
    return "".join([random.choice(symbols) for i in range(maxlen)])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    tel_home="", tel_mobile="", tel_work="", tel_fax="", email1="", email2="", email3="", homepage="",
                    bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", group="[none]", address2="",
                    phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 10), company=random_string("company", 10),
                       address=random_string("address", 10), tel_home=random_tel(10),
                       tel_mobile=random_tel(10), tel_work=random_tel(10), tel_fax=random_tel(10),
                       email1=random_string("email1", 10), email2=random_string("email2", 10),
                       email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                       bday=str(random.randrange(31)), bmonth=random.choice(calendar.month_name[1:13]),
                       byear=random.randrange(1900, 2020), aday=str(random.randrange(31)),
                       amonth=random.choice(calendar.month_name[1:13]), ayear=random.randrange(1900, 2050),
                       group="random", address2=random_string("address2", 10), phone2=random_tel(10),
                       notes=random_string("notes", 10))
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
