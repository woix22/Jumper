class Player:
    """The user playing this game. 
    
    The responsibility of the player is to guess the word, having 4 opportunities to do so.
    
    Attributes:
        lives (int): The amount of opportunities the player has to guess the word.
        guesses (list): all the guesses given by the player
    """
    def __init__(self):
        """Constructs a new Player.

        Args:
            self (Player): An instance of Player.
        """
        self._lives = 4
        self._guesses = []
        
    def lose_life(self):
        """loses a life.

        Args:
            self (Player): An instance of Player.
        """
        self._lives -= 1

    def get_lives(self):
        """Gets the current lives.
        
        Returns:
            number: The current lives,
        """
        
        return self._lives

    def set_guesses(self,guess):
        """Store the guess in the list.

        Args:
            self (Player): An instance of Player.
            guess (string): the guess by the player
        """
        self._guesses.append(guess)

    def get_guesses(self):
        """Gets the current guesses.
        
        Returns:
            list: The current guesses,
        """
        return self._guesses
