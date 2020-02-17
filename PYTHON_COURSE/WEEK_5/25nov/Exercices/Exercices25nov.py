# Exercise 1

class Family:
    def __init__(self, members, last_name):
        self.last_name = last_name
        self.members = members

    @staticmethod
    def get_from_dic(data,key,value):
    for element in data:
        if element.get(key) == value:
            return element
    return None

    def born(self, **kwargs):
        self.members.append(kwargs)

    def is_18(self, member_name):
        return self.get_from_dic(self.members, 'name', member_name)['age'] >= 18

    def __repr__(self):
        pres = ''
        for member in self.members:
            pres += ' '.join([member['name'], self.last_name, str(member['age'])]) + '\n'
        return pres


class Incredibles(Family):
    def incredible_presentation(self):
        for member in self.members:
            print(member['incredible_name'],member.get('power'))

    def use_power(self,member_name):
        member = self.get_from_dic(self.members,'name')
        if member and self.is_18(member_name):
            print(member['power'] + ' !!')
        elif not self.is_18(member_name):
            print('You have no power here !!')
        else:
            raise Exception('Member not Found')

if __name__ == '__main__':
    fam_dic = [
    {'name':'Avraham','age':100,'sex':'Male','is_child':False},
    {'name':'Sarah','age':91,'sex':'Female','is_child':False},
    {'name':'Yishma\'el','age':14,'sex':'Male','is_child':True},
    ]
fam = Family(fam_dic,last_name='Ben Tarah\'')
print(fam)
print(fam.is_18('Yishma\'el'))