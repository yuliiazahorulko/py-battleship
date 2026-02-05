class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start: tuple, end: tuple, is_drowned: bool = False) -> None:
        self.decks = []
        self.decks.append(Deck(start, end, is_drowned))
        # Create decks and save them to a list `self.decks`
        pass

    def get_deck(self, row: int, column: int) -> Deck:
        return [deck
                for deck in self.decks
                if deck.row == row
                and deck.column == column
                ][0]
        # Find the corresponding deck in the list
        # pass

    def fire(self, row, column):
        # Change the `is_alive` status of the deck
        # And update the `is_drowned` value if it's needed
        pass

    def get_points(self) -> list:
        # for s in ships:
        # horizontal ship
        s = self.start, self.end
        if s[0][0] == s[1][0]:
            temp = list(range(s[0][1], s[1][1] + 1))
            for t in temp:
                self.field[(s[0][0], t)] = Ship(s[0], s[1])
        # vertical ship
        elif s[0][1] == s[1][1]:
            temp = list(range(s[0][0], s[1][0] + 1))
            for t in temp:
                self.field[(t, s[1][1])] = Ship(s[0], s[1])
        else:
            self.field[s[0][0], s[0][1]] = Ship(s[0], s[1])


class Battleship:
    def __init__(self, ships: list) -> None:
        self.field = {}

        for s in ships:
            # horizontal ship
            if s[0][0] == s[1][0]:
                temp = list(range(s[0][1], s[1][1] + 1))
                for t in temp:
                    self.field[(s[0][0], t)] = Ship(s[0], s[1])
            # vertical ship
            elif s[0][1] == s[1][1]:
                temp = list(range(s[0][0], s[1][0] + 1))
                for t in temp:
                    self.field[(t, s[1][1])] = Ship(s[0], s[1])
            else:
                self.field[s[0][0], s[0][1]] = Ship(s[0], s[1])
        # Create a dict `self.field`.
        # Its keys are tuples - the coordinates of the non-empty cells,
        # A value for each cell is a reference to the ship
        # which is located in it
        pass

    def _validate_field(self) -> None:
        pass

    def fire(self, location: tuple) -> str:
        if location in self.field.keys():
            print("location", location)
            if self.field[location].get_deck(location[0], location[1]).is_alive is True:
                print("location is tryue")
                counter = len(self.field[location].decks)
                for ship in self.field[location].decks[:-1]:
                    if ship.is_alive is False:
                        counter -= 1

                if counter == 1:
                    return "Sunk!"
                else:
                    return "Hit!"
            return "Hit!"
        return "Miss!"

    def print_field(self):
        pass


battle_ship = Battleship(ships=[((2, 0), (2, 3)), ((4, 5), (4, 6)), ((3, 8), (3, 9)), ((6, 0), (8, 0)), ((6, 4), (6, 6)), ((6, 8), (6, 9)), ((9, 9), (9, 9)),
                                ((9, 5), (9, 5)),
                                ((9, 3), (9, 3)),
                                ((9, 7), (9, 7)),
                                ]
                        )
print(battle_ship.fire((0, 4)))
print(battle_ship.fire((1, 7)))
print(battle_ship.fire((2, 0)))
