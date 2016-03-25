'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
import collections
class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.friends = collections.defaultdict(set)
        self.user_tweets = collections.defaultdict(list)
        self.order = 0


    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        tw = Tweet.create(user_id, tweet_text)
        self.order += 1
        self.user_tweets[user_id].append((self.order, tw))
        return tw

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        ans = []
        ans.extend(self.getNewsFeedTen(user_id))
        for frindId in self.friends[user_id]:
            ans.extend(self.getNewsFeedTen(frindId))
        ans.sort(key = lambda x: x[0])
        return [v[1] for v in ans[-1:-11:-1]]
        
    def getNewsFeedTen(self, user_id):
        if user_id not in self.user_tweets:
            return []
        else:
            return self.user_tweets[user_id][-1:-11:-1]     
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        ans = self.getNewsFeedTen(user_id)
        return [v[1] for v in ans]

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        self.friends[from_user_id].add(to_user_id)

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if to_user_id in self.friends[from_user_id]:
            self.friends[from_user_id].remove(to_user_id)
        
