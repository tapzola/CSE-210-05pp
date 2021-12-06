from game.scripting.action import Action
from game.shared.point import Point


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        score.set_text("Player 1: ")
        score.set_position(Point(200, 0))
        score_2 = cast.get_first_actor("scores_2")
        score_2.set_text("Player 2: ")
        score_2.set_position(Point(600, 0))
        #food = cast.get_first_actor("foods")
        cycle = cast.get_first_actor("cycles")
        cycle_2 = cast.get_first_actor("cycles_2")
        segments = cycle.get_segments()
        segments_2 = cycle_2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        #self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments_2)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(score_2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()