#!/usr/bin/python3
"""
Module définissant une classe Rectangle avec représentation visuelle.

Ce module étend la classe Rectangle avec des fonctionnalités
de calcul d'aire et de périmètre, ainsi qu'une représentation
visuelle en chaîne de caractères pour l'affichage.
"""


class Rectangle:
    """
    Classe représentant un rectangle avec largeur, hauteur et affichage.

    Cette classe implémente un rectangle avec:
    - Attributs width et height encapsulés par des propriétés
    - Validation des types et valeurs lors de l'affectation
    - Méthodes pour calculer l'aire et le périmètre
    - Représentation visuelle du rectangle avec des symboles #
    """

    def __init__(self, width=0, height=0):
        """
        Initialise une nouvelle instance de Rectangle.

        Args:
            width (int, optional): Largeur du rectangle. Par défaut 0.
            height (int, optional): Hauteur du rectangle. Par défaut 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Propriété getter pour la largeur du rectangle.

        Returns:
            int: La largeur actuelle du rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Propriété getter pour la hauteur du rectangle.

        Returns:
            int: La hauteur actuelle du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Propriété setter pour définir la hauteur du rectangle.

        Args:
            value (int): Nouvelle hauteur à affecter

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Propriété setter pour définir la largeur du rectangle.

        Args:
            value (int): Nouvelle largeur à affecter

        Raises:
            TypeError: Si value n'est pas un entier
            ValueError: Si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            int: Surface du rectangle (width × height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            int: Périmètre du rectangle (2 × (width + height))
            ou 0 si l'une des dimensions est nulle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une représentation visuelle du rectangle avec des #.

        Cette méthode spéciale est appelée automatiquement lors de
        la conversion de l'objet en chaîne (print, str()).

        Returns:
            str: Représentation visuelle du rectangle ou chaîne vide
            si width ou height est 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        row = "#" * self.__width + "\n"
        return row * (self.__height - 1) + "#" * self.__width
