// BOJ#2480 주사위 세 개
// 조건문

package basics;

import java.io.*;

public class ThreeDices {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		String[] input = str.split(" ");
		
		int num1 = Integer.parseInt(input[0]);
		int num2 = Integer.parseInt(input[1]);
		int num3 = Integer.parseInt(input[2]);
		
		int reward = 0;
		
		if (num1==num2 && num2==num3) {
			reward = 10000 + num1*1000;
		}
		else {
			if(num1==num2 | num1==num3) reward = 1000 + num1*100;
			else if(num2 == num3) reward = 1000 + num2*100;
			else {
				int max = num1;
				if (max < num2) max = num2;
				if(max<num3) max = num3;
				reward = max*100;
			}
		}
		
		System.out.println(reward);
			
	}

}
