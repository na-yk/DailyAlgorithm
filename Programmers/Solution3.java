import java.util.*;

public class Solution1 {

    // 테스트케이스
    static int[] ns = {4, 9};
    static String[][] placelists = {
            {"부산", "프랑스", "서울", "대전", "대구", "이탈리아"},
            {"b", "a", "aa", "bb", "aaa", "bbb", "aaaa", "bbbb", "aaaaa", "bbbbb"}
    };
    static String[][] rinos = {
            {"부산", "서울", "대전", "대구"},
            {"b", "bb", "bbb", "bbbb", "bbbbb"}
    };

    static Set<String> rinoSet;
    public static void main(String[] args) {

        for(int i=0;i<ns.length;i++) {
            System.out.format("answer=%d\n",solution(ns[i], rinos[i], placelists[i]));
        }

    }

    private static int solution(int n, String[] rino, String[] placelist) {
        int answer = 0;
        boolean flag = false;

        rinoSet = new HashSet<>(Arrays.asList(rino));

        for(int x = 0;x< placelist.length-1;x++) {
//            System.out.format("======x: %d\n",x);
            if (available(n, x, placelist)){
                answer = x;
                flag = true;
//                System.out.println(answer);
                break;
            }
//            Set<String> excepts = new HashSet<>();
//            excepts.add(placelist[x+1]);
//            System.out.println(placelist[getNext(n, x, placelist, excepts)]);
        }

        if (flag) {
            return answer;
        } else{
            return -1;
        }
    }

    private static boolean available(int n, int x, String[] placelist) {
        int remain = placelist.length;
        int cur = x;
        Set<String> excepts = new HashSet<>();
        while(remain > n) {
//            System.out.println(placelist[cur]);
            if (rinoSet.contains(placelist[cur])){
                return false;
            }
            else {
                excepts.add(placelist[cur]);
                remain-=1;
            }
            cur = getNext(n, cur, placelist, excepts);
//            System.out.format("n=%d / remain=%d\n", n, remain);
        }

        return true;
    }

    private static int getNext(int n, int cur, String[] placelist, Set<String> excepts){
        int cnt = 0;
        int next = cur;

        while(cnt < n) {
            next+=1;
//            System.out.println(next);

            if (next <= placelist.length-1) {
                if(excepts.contains(placelist[next])){
                    continue;
                }
                else{
                    cnt+=1;
                }
            }
            else {
                next = 0;
                if(excepts.contains(placelist[next])) {
                    continue;
                }
                else{
                    cnt+=1;
                }
            }
//            System.out.println(placelist[next]);
//            System.out.println(cnt);
        }

        return next;

    }

}
