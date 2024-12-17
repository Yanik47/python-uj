from node import Node

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # długość listy
        self.head = None  # pierwszy węzeł
        self.tail = None  # ostatni węzeł

    def is_empty(self):
        """Sprawdza, czy lista jest pusta."""
        return self.head is None

    def count(self):
        """Zwraca długość listy."""
        return self.length

    def insert_head(self, node):
        """Wstawia węzeł na początek listy."""
        if self.head:   # lista nie jest pusta
            node.next = self.head
            self.head = node
        else:   # lista jest pusta
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        """Wstawia węzeł na koniec listy."""
        if self.head:   # lista nie jest pusta
            self.tail.next = node
            self.tail = node
        else:   # lista jest pusta
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        """Usuwa pierwszy węzeł listy."""
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # tylko jeden element w liście
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie połączenia
        self.length -= 1
        return node   # zwraca usunięty węzeł
    
    def remove_tail(self):  # klasy O(n)
        """Usuwa ostatni węzeł listy."""
        if self.is_empty():
            raise ValueError("pusta lista")
        if self.head == self.tail:  # tylko jeden element
            node = self.head
            self.head = self.tail = None
            self.length -= 1
            return node
        
        # Znajdź przedostatni węzeł
        current = self.head
        while current.next != self.tail:
            current = current.next
        node = self.tail
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return node

    def join(self, other):  # klasy O(1)
        """Łączy bieżącą listę z inną listą."""
        if not isinstance(other, SingleList):
            raise TypeError("Oczekiwano obiektu klasy SingleList")
        
        if not other.is_empty():  # tylko jeśli druga lista nie jest pusta
            if self.is_empty():   # jeśli aktualna lista jest pusta
                self.head = other.head
                self.tail = other.tail
            else:  # dopinamy węzły z `other` na koniec
                self.tail.next = other.head
                self.tail = other.tail
            self.length += other.length
            other.clear()  # czyszczenie listy other

    def clear(self):
        """Czyści listę."""
        self.head = self.tail = None
        self.length = 0

    def __iter__(self):
        """Iteruje po danych listy."""
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        """Zwraca reprezentację listy jako ciąg znaków."""
        return " -> ".join(str(node) for node in self)
