"""
An AI that uses Finite State Machines to solve a maze

@author: Aidan Housenbold
@version: 2022
"""
from fsm import FSM


class MazeBot:
    def __init__(self, maze_file):
        # The location of the bot
        self.x = None
        self.y = None

        # The map of the maze
        self.maze = None

        # The route the bot will take to get to the $
        self.path = None

        # Create an initialize the maze
        self.reset(maze_file)


        self.fsm = FSM("NSouth")
        self.add_state_transitions()


    def add_state_transitions(self):
        """
        Adds all the state transitions to the fsm
        """
        #Breaker to Neutral
        self.fsm.add_transition("B", "BNorth", self.move_north, "NNorth")
        self.fsm.add_transition("B", "BSouth", self.move_south, "NSouth")
        self.fsm.add_transition("B", "BEast", self.move_east, "NEast")
        self.fsm.add_transition("B", "BWest", self.move_west, "NWest")

        #neutral to breaker
        self.fsm.add_transition("B", "NNorth", self.move_north, "BNorth")
        self.fsm.add_transition("B", "NSouth", self.move_south, "BSouth")
        self.fsm.add_transition("B", "NEast", self.move_east, "BEast")
        self.fsm.add_transition("B", "NWest", self.move_west, "BWest")

        #Breaker --> #
        self.fsm.add_transition("#", "BNorth", None, "BWest")
        self.fsm.add_transition("#", "BSouth", None, "BEast")
        self.fsm.add_transition("#", "BEast", None, "BNorth")
        self.fsm.add_transition("#", "BWest", None, "BSouth")

        # Nuetral --> #
        self.fsm.add_transition("#", "NNorth", None, "NWest")
        self.fsm.add_transition("#", "NSouth", None, "NEast")
        self.fsm.add_transition("#", "NEast", None, "NNorth")
        self.fsm.add_transition("#", "NWest", None, "NSouth")

        # Nuetral --> $
        self.fsm.add_transition("$", "NNorth", None, "FIN")
        self.fsm.add_transition("$", "NSouth", None, "FIN")
        self.fsm.add_transition("$", "NEast", None, "FIN")
        self.fsm.add_transition("$", "NWest", None, "FIN")

        # Breaker --> $
        self.fsm.add_transition("$", "BNorth", None, "FIN")
        self.fsm.add_transition("$", "BSouth", None, "FIN")
        self.fsm.add_transition("$", "BEast", None, "FIN")
        self.fsm.add_transition("$", "BWest", None, "FIN")

        # Breaker --> " "
        self.fsm.add_transition(" ", "BNorth", self.move_north, "BNorth")
        self.fsm.add_transition(" ", "BSouth", self.move_south, "BSouth")
        self.fsm.add_transition(" ", "BEast", self.move_east, "BEast")
        self.fsm.add_transition(" ", "BWest", self.move_west, "BWest")

        # neutral --> " "
        self.fsm.add_transition(" ", "NNorth", self.move_north, "NNorth")
        self.fsm.add_transition(" ", "NSouth", self.move_south, "NSouth")
        self.fsm.add_transition(" ", "NEast", self.move_east, "NEast")
        self.fsm.add_transition(" ", "NWest", self.move_west, "NWest")

        # Breaker --> X
        self.fsm.add_transition("X", "BNorth", self.move_north, "BNorth")
        self.fsm.add_transition("X", "BSouth", self.move_south, "BSouth")
        self.fsm.add_transition("X", "BEast", self.move_east, "BEast")
        self.fsm.add_transition("X", "BWest", self.move_west, "BWest")

        # Nuetral --> X
        self.fsm.add_transition("X", "NNorth", None, "NWest")
        self.fsm.add_transition("X", "NSouth", None, "NEast")
        self.fsm.add_transition("X", "NEast", None, "NNorth")
        self.fsm.add_transition("X", "NWest", None, "NSouth")


    def reset(self, filename):
        """
        Resets the maze bot to have an empty path and sets the maze
        from the given filename. The bot starts at position 1, 1
        :param filename: The name of the file to read the maze in from
        """
        # The bot always starts at the Northwest corner of the maze
        self.x = 1
        self.y = 1

        # The path resets to empty
        self.path = []

        # Read in the maze from the file
        self.maze = []
        with open(filename) as f:
            line = f.readline().strip()
            self.maze.append(line)
            while line:
                line = f.readline().strip()
                self.maze.append(line)

    def move_south(self):
        """
        Changes the bot's location 1 spot South
        and records the movement in self.path
        """
        self.y += 1
        self.path.append("South")

    def move_east(self):
        """
        Changes the bot's location 1 spot East
        and records the movement in self.path
        """
        self.x += 1
        self.path.append("East")

    def move_north(self):
        """
        Changes the bot's location 1 spot North
        and records the movement in self.path
        """
        self.y -= 1
        self.path.append("North")

    def move_west(self):
        """
        Changes the bot's location 1 spot West
        and records the movement in self.path
        """
        self.x -= 1
        self.path.append("West")

    def get_next_space(self):
        """
        Using the current state of the bot, returns the next space in the maze
            Ex. If the current state has the bot moving south, the next space in the
            maze would be self.maze[self.y+1][self.x]
        :return: The next spot in the maze Ex. "B", "#", " ", "X"
        """
        if self.fsm.current_state == "NSouth" or self.fsm.current_state == "BSouth":
            return self.maze[self.y + 1][self.x]
        elif self.fsm.current_state == "NNorth" or self.fsm.current_state == "BNorth":
            return self.maze[self.y - 1][self.x]
        elif self.fsm.current_state == "NWest" or self.fsm.current_state == "BWest":
            return self.maze[self.y][self.x - 1]
        elif self.fsm.current_state == "NEast" or self.fsm.current_state == "BEast":
            return self.maze[self.y][self.x + 1]

    def print_maze(self):
        """
        Prints the 2D array representing the maze
        Prints an 'M' for the current location of the bot in the maze
        """
        for row in range(len(self.maze)):
            curr = ''
            for col in range(len(self.maze[row])):
                if row == self.y and col == self.x:
                    curr += 'M'
                else:
                    curr += self.maze[row][col]
            print(curr)

    def solve_maze(self):
        """
        Calls on the FSM to process the next input symbol from the maze
        in order to transition the bot between states until it reaches the "FIN" state
        """

        while self.fsm.current_state != "FIN":
            self.print_maze()
            temp = self.get_next_space()
            self.fsm.process(self.get_next_space())
        print("Determined the path:")
        print(self.path)
