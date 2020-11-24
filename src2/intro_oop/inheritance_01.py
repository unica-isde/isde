class Contact:

    def __init__(self, name, email):
        self.name = name
        if self._validate_mail(email):
            self.email = email
        else:
            self.email = '(missing email)'

    def who_I_am(self):
        return self.name + ' ' + self.email

    @staticmethod
    def _validate_mail(email):
        name_domain = email.split('@')
        if len(name_domain) != 2:
            return False
        name, domain = name_domain
        # al least 1 character in the name and 4 in the domain, i.e.  a@b.it
        if len(name) < 1 or len(domain) < 4:
            return False
        return True


class Supplier(Contact):
    def order(self, an_order):
        print("this is your order: ", an_order)


class Friend(Contact):
    def __init__(self, name, email, phone=''):
        super().__init__(name, email)
        self.phone = phone


if __name__ == '__main__':
    c = Contact('John Red', 'john@gmail.com')
    s = Supplier('Jim Black', 'jim@gmail.com')
    f1 = Friend('Sue Whita', 'sue@gmail.com', '123123')
    f2 = Friend('Ann Gray', 'ann.gmail.com', '777777')

    print(c.who_I_am())
    print(s.who_I_am())
    print(f1.who_I_am())
    print(f2.who_I_am())
    print(f2.phone)
    s.order('a_thing')
