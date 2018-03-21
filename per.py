class Person:
    def __init__(self,name,age,anger):
        self.name=name
        self.age=age
        self.anger=anger

    def say(self,word):
        print('{}说{}'.format(self.name,word))


if __name__ == '__main__':
    p = Person('xiaoming',18,97)
    p.say('python很简单')