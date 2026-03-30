class Twitter:

    def __init__(self):
        self.tweet_map, self.follow_map = {}, {}     
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # user_id : [(count, tweetID), ...], we want ot append a tweet and updated count to hte map
        # check if the user exizts in our map if thye do not then initzlie hte tuple, else append the new one ot the list
        self.count += 1
        if userId not in self.tweet_map:
            self.tweet_map[userId] = []
        self.tweet_map[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        
        # Get all users to check (user + followees)
        users_to_check = self.follow_map.get(userId, set()).copy()
        users_to_check.add(userId)
        
        # Add most recent tweet from each user
        for user in users_to_check:
            if user in self.tweet_map and len(self.tweet_map[user]) > 0:
                idx = len(self.tweet_map[user]) - 1
                count, tweetId = self.tweet_map[user][idx]
                heapq.heappush(heap, (-count, tweetId, user, idx))
        
        # Pop 10 most recent tweets
        while heap and len(res) < 10:
            count, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            
            # Add next tweet from this user if exists
            if idx > 0:
                next_idx = idx - 1
                count, tweetId = self.tweet_map[user][next_idx]
                heapq.heappush(heap, (-count, tweetId, user, next_idx))
        
        return res

        
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
#         followerId: The person who is doing the following (the user initiating the action)
#         followeeId: The person being followed (the target)
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set()
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
     
