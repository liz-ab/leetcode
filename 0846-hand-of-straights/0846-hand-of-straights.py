class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize!=0:
            return False
        map=Counter(hand)
        hand.sort()
        i=0
        for j in range(len(hand)):
            n=hand[i]
            while n not in map:
                i+=1
                n=hand[i]
            for x in range (groupSize):
                if n+x not in map:
                    return False
            for x in range (groupSize):
                map[n+x]-=1
                if map[n+x]==0:
                    del map[n+x]
            if not map:
                return True

        