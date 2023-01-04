// BOJ#1546 평균
// 1차원 배열

package basics;

import java.io.*;

public class Average {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		
		String[] score = str.split(" ");
		
		int max = 0;	//가장 높은 점수 구하기
		for (int i=0;i<n;i++) {	
			if(max<Integer.parseInt(score[i])) {
				max = Integer.parseInt(score[i]);
			}
		}

		float new_score = 0;
		float cur_score = 0;
		
		float total = 0; 	//새로운 점수 합
		for (int i=0;i<n;i++) {
			cur_score = Float.parseFloat(score[i]);
			new_score = cur_score/max*100;
			total= total+new_score;
		}
		
		double avg = total/n;
		System.out.printf("%.6f\n",avg);
		
	}

}
