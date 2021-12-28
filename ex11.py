from typing import List
from numpy import median
import doctest

def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    
    """
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100]]
    >>> compute_budget(100, citizen_votes)
    [50.0, 0.0, 50.0]
    """
    z,o = 0,1
    while z <= o:
        mid=(z+o)/2
        votes,ans=[total_budget*min(1,i*mid) for i in range(1,len(citizen_votes))],[]
        for i in range(len(citizen_votes[0])):
            new_votes=[]
            for c in citizen_votes:
                new_votes.append(c[i])
            for v in votes:
                new_votes.append(v)
            ans.append(median(new_votes)) 
        if sum(ans)>total_budget: 
            o=mid  #search in the lower part
        elif  sum(ans)<total_budget:
            z=mid  #search in the higher part
        else:
            return ans

if __name__ == '__main__':
  
    failures, tests = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))