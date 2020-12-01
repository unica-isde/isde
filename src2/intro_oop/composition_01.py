class AlternateList_comp:
    def __init__(self):
        self.values = []
        self.accept = True

    def add_item(self, v):
        if self.accept:
            self.values.append(v)
        self.accept = not self.accept

    def add_collection(self, v_collection):
        for v in v_collection:
            self.add_item(v)


class AlternateList_inh(list):
    def __init__(self):
        super().__init__(self)
        self.accept = True

    def add_item(self, v):
        if self.accept:
            self.append(v)
        self.accept = not self.accept

    def add_collection(self, v_collection):
        for v in v_collection:
            self.add_item(v)


obj1_comp = AlternateList_comp()
obj2_comp = AlternateList_comp()
obj1_inh = AlternateList_inh()
obj2_inh = AlternateList_inh()
n = 21
for i in range(1, n):
    obj1_comp.add_item(i)
    obj1_inh.add_item(i)

obj2_comp.add_collection(list(range(1, n)))
obj2_inh.add_collection(list(range(1, n)))

print(obj1_comp.values)
print(obj2_comp.values)
print(obj1_inh)
print(obj2_inh)
