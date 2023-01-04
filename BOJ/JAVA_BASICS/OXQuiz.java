// BOJ#8958 OX퀴즈
// 1차원 배열

package basics;

import java.io.*;

public class OXQuiz {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine()); //테스트 케이스 개수
		
		int score[] = new int[n]; //각 테스트케이스의 점수를 저장할 배열
		int bonus = 0;	//연속으로 정답일 때 추가점수 계산
		
		for(int i=0;i<n;i++) {
			String str = br.readLine();
			score[i] = 0;	//현재 테스트케이스 총점은 0에서 시작
			bonus = 0;	//연속 정답 추가점수 초기화
			for (int j=0;j<str.length();j++) {
				if (str.charAt(j) == 'O') {	//정답일 경우
					bonus+=1;	//bonus에 1 더함(연속 정답 개수만큼 올라감)
					score[i]+=bonus; //현재 테스트케이스의 총점에 더함 
				}
				else if (str.charAt(j) == 'X'){	//오답일 경우
					bonus = 0; //연속 정답일 때의 추가점수 초기화
				}
			}
		}
		
		for(int i=0;i<n;i++) { // 저장된 총점 모두 출력
			System.out.println(score[i]);
		}
	}
}

