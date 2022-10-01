class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def print_parachute(self,lives):
        """prints the parachute according to the player's number of lives.

        Args: 
            self (TerminalService): An instance of TerminalService.
            lives (int): The player's lives.
        """
        parachute = ["  ___", " /___\\", " \\   /", "  \\ /",
                     "   O", "  /|\\", "  / \\", "", "^^^^^^^"]

        if lives == 3:
            parachute.pop(0)
        elif lives == 2:
            for i in range(2):
                parachute.pop(0)

        elif lives == 1:
            for i in range(3):
                parachute.pop(0)

        elif lives == 0:
            for i in range(4):
                parachute.pop(0)
            parachute[0] = "   x"

        for i in parachute:
            print(i)

    def print_puzzle(self,puzzle):
        word = ""
        for i in puzzle:
            word += i
        print(f"\n{word}\n")
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def validate_answer(self,answer):
        """validates whether the answer given by the user is valid or not.

        Args: 
            self (TerminalService): An instance of TerminalService.
            answer (string): The answer given by the user.

        Returns:
            boolean: True or False.
        """
        valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"       
        if answer not in valid_characters:
            print("Invalid input")  
            return False
        elif len(answer) > 1:
            print("Invalid input")
            return False
        return True  
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)