class Category:
    def __init__(self, name):
        self.ledger = []
        self.total = 0
        self.withdrawl = 0
        self.name = name
        
    def __str__(self):
        pr = ''
        l = 30 - len(self.name)
        if l%2 == 0:
            fr = bk = int(l/2)
        else:
            fr = int(l/2) + 1
            bk = int(l/2)
        pr += ('*')*fr + self.name + ('*')*bk + '\n'
        for i in range(len(self.ledger)):
            values = list(self.ledger[i].values())
            des = values[1]
            amount = values[0]
            if len(des) > 23:
                des = des[:23]
            sp = 23 - len(des)
            s = ' '*sp
            k = "{:.2f}".format(amount)
            pr += f'{des}{s}{str(k).rjust(7)}\n'
        total_fl = "{:.2f}".format(self.total)
        pr += f'Total: {total_fl}'
        return pr
    
    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.total -= amount
            self.withdrawl += amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        return float("{:.2f}".format(self.total))
    
    def transfer(self, amount, category):
        s = category.name
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {s}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
        



def create_spend_chart(categories):
    tens_list = ['100','90','80','70','60','50','40','30','20','10','0']
    p = "Percentage spent by category"
    w = []
    names = []
    total = 0
    for i in categories:
        w.append(i.withdrawl)
        names.append(i.name)
        total += i.withdrawl
    for row in tens_list:
        p += '\n'+(row+'| ').rjust(5)
        for i in range(len(names)):
            o = ' '
            if ((w[i]/total)*100) >= int(row):
                o = 'o'
            p += o + '  '
    p += '\n    ' + ('---'*len(names))+'-'
    m = 0
    for i in names:
        m = max(m, len(i))
    for row in range(m):
        p += '\n     '
        for name in names:
            try:
                l = name[row]
            except:
                l = ' '
            p += l+'  '
    return p
