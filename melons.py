"""This file should have our melon-type classes in it."""


class Melon(object):
    species = None
    color = None
    imported = None
    shape = None
    seasons = []

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if self.species == "Casabas" or self.species == "Ogens":
            self.price = self.price + 1.0

        if self.imported: 
            self.price = self.price * 1.5

        if self.shape == "square":
            self.price = self.price * 2.0

        total = self.price * qty

        if self.species == "Watermelon" and qty >= 3:
            total = total * 0.75
        elif self.species == "Cantaloupe" and qty >= 5:
            total = total * 0.50



        return total

class WatermelonOrder(object):
    species = 'Watermelon'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    