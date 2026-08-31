class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev,curr = head,head.next
        index = 1
        minimum = sys.maxsize
        prevCP = firstCP = 0

        while curr.next:
            pVal,cVal = prev.val,curr.next.val
            if(curr.val<min(pVal,cVal) or curr.val>max(pVal,cVal)):
                if prevCP: minimum = min(minimum,index-prevCP)
                else: firstCP = index
                prevCP = index    
            prev = curr
            curr = curr.next
            index+=1
        
        return [minimum,prevCP-firstCP] if minimum!=sys.maxsize else [-1,-1]