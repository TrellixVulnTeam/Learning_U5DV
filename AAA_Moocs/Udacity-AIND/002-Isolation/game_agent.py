
"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
from operator import itemgetter


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    This should be the best heuristic function for your project submission.
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return float(len(game.get_legal_moves(player)))
    
    


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player) or game.is_winner(player):
        return game.utility()

    return float(len(game.get_legal_moves())) / float(len(game.get_legal_moves(game.get_opponent(player))))


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.
    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)
    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    if game.is_loser(player) or game.is_winner(player):
        return game.utility()

    # Calculate the centrality score for a given state
    ctr_x, ctr_y = game.width / 2. , game.height / 2.
    x,y = game.get_player_location(player)
    
    return float((ctr_y - y) + (ctr_x - x))



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.
    ********************  DO NOT MODIFY THIS CLASS  ********************
    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)
    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.
    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************
        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move
    

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.
        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        
        def max_value(self, game, depth):
            
            """Helper function to implement the maximum function
    
            Parameters
            ----------
            game : isolation.Board
                An instance of the Isolation game `Board` class representing the
                current game state
    
            depth : int
                Depth is an integer representing the maximum number of plies to
                search in the game tree before aborting
                
                
            Returns
            -------
            float
                The utility of the game state when depth == 1 or the game has ended
            
            """
            # Checking for Timeout
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            # Check if game has ended / reached Max Depth
            if depth == 1 or not game.get_legal_moves():
                return self.score(game, self)

            max_v = float('-inf')
            max_v =  max([min_value(self, game.forecast_move(m), depth-1) for m in game.get_legal_moves()])
            
            return max_v
        
        def min_value(self, game, depth):
            
            """Helper function to implement the maximum function
    
            Parameters
            ----------
            game : isolation.Board
                An instance of the Isolation game `Board` class representing the
                current game state
    
            depth : int
                Depth is an integer representing the maximum number of plies to
                search in the game tree before aborting
                
                
            Returns
            -------
            float
                The utility of the game state when depth == 1 or the game has ended
            
            """
            # Checking for Timeout
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            
            # Check if game has ended / reached Max Depth
            if depth == 1 or not game.get_legal_moves():
                return self.score(game, self)

            min_v = float('-inf')
            min_v = min([max_value(self, game.forecast_move(m), depth-1) for m in game.get_legal_moves()])
            return min_v
            
    
        # Implementing the MinMax Depth Limited Algorithm 
        scored_moves = [(m, min_value(self, game.forecast_move(m), depth)) for m in game.get_legal_moves()]
        
        # Selecting the max_move from the scored list based on its value
        return max(scored_moves, key=itemgetter(1))[0]
        

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.
        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!

        # Initialize move to be returned in case of timeout
        best_move = (-1, -1)

        # Catching the SearchTimeout Exception and returning the current
        # best_move instead
        depth = 1
        try:
            while True:
                # While there is time, iterate ever deeper over the possible search space
                best_move = self.alphabeta(game, depth)
                depth += 1
        except SearchTimeout:
            return best_move

        # If best_move was found a
        return best_move

    def maxvalue(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Check if maxdepth is reached or game over
        if depth <= 0 or not game.get_legal_moves():
            return self.score(game, self)

        max_v = float("-inf")
        # Search for the best maximizing move for the given state
        for m in game.get_legal_moves():
            max_v = max(max_v, self.minvalue(game.forecast_move(m), depth-1, alpha, beta))
            if max_v >= beta:
                return max_v
            alpha = max(max_v, alpha)
        return max_v

    def minvalue(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Check if maxdepth is reached or game over
        if depth <= 0 or not game.get_legal_moves():
            return self.score(game, self)
            
        min_v = float("inf")
        # Search for the best minimizing move for the given state
        for m in game.get_legal_moves():
            min_v = min(min_v, self.maxvalue(game.forecast_move(m), depth-1, alpha, beta))
            if min_v <= alpha:
                return min_v
            beta = min(min_v, beta)
        return min_v

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.
        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        alpha : float
            Alpha limits the lower bound of search on minimizing layers
        beta : float
            Beta limits the upper bound of search on maximizing layers
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return (-1, -1)

        if len(game.get_legal_moves()) > 0:
            best_move = game.get_legal_moves()[0]
        else:
            best_move = (-1, -1)
        max_score = float("-inf")
        score = float("-inf")

        for m in game.get_legal_moves():
            score = self.minvalue(game.forecast_move(m), depth-1, alpha, beta)
            if score > max_score:
                max_score = score
                best_move = m
            alpha = max(max_score, alpha)
        return best_move