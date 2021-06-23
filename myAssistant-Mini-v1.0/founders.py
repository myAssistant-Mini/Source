class Person:
    def __init__(self, name: str):
        self.name = name
        self.creator_information = []

    def get_name(self):
        return self.name

    def set_info(self, information: str):
        self.creator_information = information.split('.')

    def get_info(self):
        return self.creator_information


atharva = Person('Atharva')
bhavesh = Person('Bhavesh')
yogesh = Person('Yogesh')
rahul = Person('Rahul')

atharva.set_info(
    ' is student of Datta Meghe College of Engineering. Loves to play cricket and hang out with his friends. took great efforts to create me.')

bhavesh.set_info(
    ' is student of Datta Meghe College of Engineering. Loves to play BasketBall and to read Books. also likes programming. took great efforts to create me.')

yogesh.set_info(
    ' is student of Datta Meghe College of Engineering. Loves to play football. is good in extra curricular activities. took great efforts to create me.')

rahul.set_info(
    ' is student of Datta Meghe College of Engineering. Loves to play cricket and hang out with his friends. took great efforts to create me.')
