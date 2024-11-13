class Contact:

    def __init__(self, name, email):
        self._name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        is_correct = self._check_email_correctness(email)
        self._email = email if is_correct else "NO EMAIL ADDRESS"

    @staticmethod
    def _check_email_correctness(email):
        splitted_address = email.split("@")
        if len(splitted_address) != 2:
            return False
        username, domainname = splitted_address
        if len(domainname) < 4:
            return False
        return True


class Supplier(Contact):

    def order(self, anOrder):
        print("this is your order: ", anOrder)


class Friend(Contact):

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


if __name__ == "__main__":
    c = Contact("pippo", "pippo@gmail.com")
    s = Supplier("pluto", "pluto@gmail.com")

    print(c.name, c.email)
    print(s.name, s.email)

    # c.order("mouse")
    # AttributeError: "Contact" object has no attribute "order"
    s.order("mouse")

    f = Friend("goofie", "goofie@gmail.com", "123123")
