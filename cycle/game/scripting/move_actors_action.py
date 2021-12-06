from game.scripting.action import Action
from game.casting.cycle import Cycle

class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycle = cast.get_first_actor("cycles")
        cycle.grow_trail(1)

        cycle_2 = cast.get_first_actor("cycles_2")
        cycle_2.grow_trail(1)
        

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()