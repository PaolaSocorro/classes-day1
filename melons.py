"""This file should have our melon-type classes in it."""


class Melon(object):
    species = None
    color = None
    imported = None
    shape = None
    seasons = []

    def get_base_price(self):
        return 5

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = self.get_base_price()
        if self.species == "Casaba" or self.species == "Ogen":
            price += 1.0

        if self.imported: 
            price *= 1.5

        if self.shape == "square":
            price *= 2.0

        total = price * qty

        if self.species == "Watermelon" and qty >= 3:
            total = total * 0.75
        elif self.species == "Cantaloupe" and qty >= 5:
            total = total * 0.50

        return total

class WatermelonOrder(Melon):
    species = 'Watermelon'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

class CantaloupeOrder(Melon):
    species = 'Cantaloupe'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

class CasabaOrder(Melon):
    species = 'Casaba'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Winter','Fall', 'Summer']

class SharlynOrder(Melon):
    species = 'Sharlyn'
    color = 'tan'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

class SantaClausOrder(Melon):
    species = 'Santa Claus'
    color = 'green'
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

class ChristmasOrder(Melon):
    species = 'Christmas'
    color = 'green'
    imported = False
    shape = 'natural'
    seasons = ['Winter']

class HornedMelonOrder(Melon):
    species = 'Horned Melon'
    color = 'yellow'
    imported = True
    shape = 'natural'
    seasons = ['Summer']

class XiguaOrder(Melon):
    species = 'Xigua'
    color = 'black'
    imported = True
    shape = 'square'
    seasons = ['Spring', 'Summer']

class OgenOrder(Melon):
    species = 'Ogen'
    color = 'tan'
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']