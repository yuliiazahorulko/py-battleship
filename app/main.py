from __future__ import annotations


class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive

    def __eq__(self, other: Deck) -> bool:
        if self.row == other.row and self.column == other.column:
            return True
        else:
            return False


class Ship:
    def __init__(self,
                 start: tuple,
                 end: tuple,
                 is_drowned: bool = False
                 ) -> None:
        """Create decks and save them to a list `self.decks`"""
        self.decks = []
        self.is_drowned = is_drowned

        # horizontal ship
        if start[0] == end[0]:
            temp = list(range(start[1], end[1] + 1))
            for temp_column in temp:
                self.decks.append(Deck(start[0], temp_column))
        elif start[1] == end[1]:
            temp = list(range(start[0], end[0] + 1))
            for temp_row in temp:
                self.decks.append(Deck(temp_row, end[1]))
        else:
            self.decks.append(Deck(start[0], start[1]))

    def __repr__(self) -> str:
        return f"Ship: {self.decks}, is_drowned={self.is_drowned}"

    def get_deck(self, row: int, column: int) -> Deck:
        """Find the corresponding deck in the list"""
        return [deck
                for deck in self.decks
                if deck.row == row
                and deck.column == column
                ][0]

    def fire(self, row: int, column: int) -> None:
        """Change the `is_alive` status of the deck
        And update the `is_drowned` value if it's needed"""
        pass


class Battleship:
    def __init__(self, ships: list) -> None:
        """ Create a dict `self.field`.
         Its keys are tuples - the coordinates of the non-empty cells,
         A value for each cell is a reference to the ship
         which is located in it """
        self.field = {}

        for some_ship in ships:
            ship = Ship(some_ship[0], some_ship[1])

            for temp_ship in ship.decks:
                self.field[(temp_ship.row, temp_ship.column)] = ship

    def _validate_field(self) -> None:
        pass

    def fire(self, location: tuple) -> str:
        """ This function should check whether the location
        # is a key in the `self.field`
        # If it is, then it should check if this cell is the last alive
        # in the ship or not. """
        if location in self.field.keys():
            if self.field[location].is_drowned is False:
                temp_deck = Deck(location[0], location[1])
                index_of_deck = self.field[location].decks.index(temp_deck)
                if self.field[location].decks[index_of_deck].is_alive:
                    self.field[location].decks[index_of_deck].is_alive = False

                    counter = len(self.field[location].decks)
                    for deck in self.field[location].decks:
                        if deck.is_alive is False:
                            counter -= 1
                    if counter == 0:
                        return "Sunk!"

                    return "Hit!"
        else:
            return "Miss!"

    def print_field(self) -> None:
        pass
