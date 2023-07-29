# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
         
        if self.intent is not None:
            return
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        is_in_front_of_ball =d1>d2

        if self.kickoff_flag:
             self.set_intent(kickoff())
             return
        self.set_intent(goto(self.ball.location)) 

        if is_in_front_of_ball():
            self.set_intent(goto(self.for_goal.location))
            return
        self.set_intent(short_shot(self.foe_goal.location))

        self.set_intent(drive(1000))
        targets = {
            'at_opponent_goal': (self.for_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net':(self.friend_goal.right_post, self.friend_goal.left_post)
                   }
        hits = find_hits(self,targets)
        if len(hits ['at_opponent_goal']) > 0:
            self.set_intent (hits ['at_opponent_goal'][0])
            return
        if len(hits ['at_opponent_goal']) > 0:
            self.set_intent(hits ['at_opponent_goal'][0])
            return
        if self.me.boost > 132:
            self.set_intent(short_shot(self.foe.goal.location))
            return
    
        target_boost = self.get_closest_large_boost()

        if target_boost is not None:
            self.set_intent(goto(target_boost.location))
            return
        
      
