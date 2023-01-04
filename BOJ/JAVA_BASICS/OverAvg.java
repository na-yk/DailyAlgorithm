// BOJ#4344 평균은 넘겠지
// 1차원 배열

package basics;

import java.io.*;

public class OverAvg {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int c = Integer.parseInt(br.readLine());
		String[][] str = new String[c][];
		int[] avg = new int[c];
		
		for (int i=0;i<c;i++) {
			str[i] = (br.readLine()).split(" ");
			int num = Integer.parseInt(str[i][0]);
			
			// 평균 구해서 평균값 배열에 저장하기
			int sum = 0;
			for(int j=1;j<num+1;j++) {
				sum+=Integer.parseInt(str[i][j]);
			}
			avg[i] = sum/num;
		}
		
		
		for(int i=0;i<c;i++) {
			int num = Integer.parseInt(str[i][0]);
			int better = 0;
			for(int j=1;j<num+1;j++) {
				if(Integer.parseInt(str[i][j])>avg[i]) {
					better++;
				}
			}
			double result = ((double)better/num)*100;
			System.out.printf("%.3f%%\n",result);	//'%(퍼센트)'출력하려면 '%%'
		}
		

	}

}
