// Last updated: 7/14/2026, 1:59:09 PM
class Solution {
    public int rob(int[] nums) {
        int p1=0,p2=0,temp;
        for(int i:nums)
        {
            temp=p1;
            p1=Math.max(p1,p2+i);
            p2=temp;
        }
      return p1;  
    }
}