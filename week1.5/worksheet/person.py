# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):

        """
        Checks the parameters match expected types and values and assigns
        them to the object's name and birth attributes.
        """
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if name.strip() == "":
            raise ValueError("Name cannot be an empty string")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date")

        self.name = name
        self.birth = birth

    def initials(self):
        """
        Returns the initials of the person's name.

        Splits the person's name into words by each space in the string.
        Iterates over each word, taking the first letter of each word and making
        it uppercase.
        Returns each initial as a string.
        """
        words = self.name.split()
        initials = []
        for i in range(0, len(words)):
            word = words[i]
            word = word[0:1].upper()
            initials.append(word)

        return ''.join(initials)

    def is_birthday(self):
        """
        Returns true if today's date is the person's birthday, otherwise false.
        """
        return (date.today().day == self.birth.day) and (date.today().month == self.birth.month)