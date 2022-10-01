import random

class Puzzle:
    """The puzzle. 
    
    Basically the puzzle is a word chosen randomly from a list.
    
    Attributes:
        words_list (list): A list of words.
        word (string): a single word.
        puzzle (list): A list with the same number of spaces as letters of the chosen word.
    """
    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._words_list = ["airplane", "biscuit", "cinnamon", "delicious", "elephant", "feather", "gorgeous", "hilarious", "illusion", "jelly", "kangaroo",
                           "language", "monster", "neon", "opera", "pancake", "queen", "rat", "studio", "trampoline", "umbrella", "violet", "wonderful", "xenon", "yoghurt", "zebra"]
        self._word = ""        
        self._puzzle = []

    def choose_word(self):
        """Choses a random word from the words list.
        
        Returns:
            boolean: True or False.
        """
        self._word = random.choice(self._words_list)
        for i in range(len(self._word)):  
            self._puzzle.append(" _ ")        

    def verify(self, letter):
        """Choses a random word from the words list.

        Args:
            self (Puzzle): An instance of Puzzle.
            letter (string): The given letter (guess).
        
        Returns:
            boolean: True or False.
        """
        letter = letter.lower()
        if letter in self._puzzle:
            return True
        elif letter in self._word:
            for i in range(len(self._word)):
                if self._word[i] == letter:
                    self._puzzle[i] = f" {letter} "
            return True
        else:
            return False

    def get_puzzle(self):
        """Gets the puzzle.
        
        Returns:
            list: Returns the puzzle list.
        """
        return self._puzzle

    def get_word(self):
        """Gets the word.
        
        Returns:
            string: Returns the word.
        """
        return self._word




