using system;

public class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if(a > b){
            for(int c = a - b; c > -1; c-- )
                answer += b + c;
        }
        else{
            for(int c = b - a; c > -1; c-- )
                answer += a + c;
        }
        return answer;
    }
}
