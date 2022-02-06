class AutomaticDoor:

    def __init__(self):
        self.state = 'Closed,Locked'
        self.out = ''

    def open(self):
        if self.state == 'Opened,Unlocked':
            self.null()
        elif self.state == 'Opened,Locked':
            self.null()
        elif self.state == 'Closed,Unlocked':
            self.state = 'Opened,Unlocked'
            self.null()
        elif self.state == 'Closed,Locked':
            self.state = 'Broken'
            self.alarm()
        elif self.state == 'Broken':
            self.null()

    def close(self):
        if self.state == 'Opened,Unlocked':
            self.state = 'Closed,Unlocked'
            self.null()
        elif self.state == 'Opened,Locked':
            self.state = 'Closed,Locked'
            self.null()
        elif self.state == 'Closed,Unlocked':
            self.null()
        elif self.state == 'Closed,Locked':
            self.null()
        elif self.state == 'Broken':
            self.null()

    def lock(self):
        if self.state == 'Opened,Unlocked':
            self.state = 'Opened,Locked'
            self.bip_2()
        elif self.state == 'Opened,Locked':
            self.null()
        elif self.state == 'Closed,Unlocked':
            self.state = 'Closed,Locked'
            self.bip_2()
        elif self.state == 'Closed,Locked':
            self.null()
        elif self.state == 'Broken':
            self.null()

    def unlock(self):
        if self.state == 'Opened,Unlocked':
            self.null()
        elif self.state == 'Opened,Locked':
            self.state = 'Opened,Unlocked'
            self.bip_1()
        elif self.state == 'Closed,Unlocked':
            self.null()
        elif self.state == 'Closed,Locked':
            self.state = 'Closed,Unlocked'
            self.bip_1()
        elif self.state == 'Broken':
            self.null()

    def null(self):
        self.out = 'NULL'

    def alarm(self):
        self.out = 'ALARM'

    def bip_1(self):
        self.out = 'BIP_1'

    def bip_2(self):
        self.out = 'BIP_2'
