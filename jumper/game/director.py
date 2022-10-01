from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.player import Player


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        player (Player): The game's player.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._player = Player()
        self._terminal_service = TerminalService()

        self._puzzle.choose_word()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._game_loop()

    def _game_loop(self):
        """A game loop that repeats everytime until the game is over.

        Args:
            self (Director): An instance of Director.
        """
        lives = self._player.get_lives()
        puzzle_word = self._puzzle.get_puzzle()
        self._terminal_service.print_puzzle(puzzle_word)
        self._terminal_service.print_parachute(lives)
        self._terminal_service.write_text(self._player.get_guesses())
        
        if lives > 0 and " _ " in puzzle_word:

            while True:
                guess = self._terminal_service.read_text(
                    "\nGuess a letter [a-z]: ")
                if self._terminal_service.validate_answer(guess):
                    break
            self._player.set_guesses(guess)
            if self._puzzle.verify(guess) != True:
                self._player.lose_life()
        else:
            self._terminal_service.write_text("\nGame Over")
            self._terminal_service.write_text(f"The word was: {self._puzzle.get_word()}")
            self._terminal_service.write_text(f"Number of guesses: {len(self._player.get_guesses())}")
            self._is_playing = False

    
