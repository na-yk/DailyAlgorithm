// BOJ#1110 더하기사이클
// 반복문

package basics;

import java.io.*;

public class PlusCycle {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int input = Integer.parseInt(br.readLine());
		int new_num = 0;
		int unit = 0;
		int tenth = 0;
		
		int cycle = 0;
		int temp = 0;
		
		do {
			if (cycle == 0) temp = input;
			else temp = new_num;
					
			if (temp < 10) unit = temp;
			else unit = (temp/10+temp%10)%10;
			tenth = temp % 10;
			new_num = tenth*10+unit;
			
			cycle+=1;
		}while(new_num != input);
		
		System.out.println(cycle);

	
	}

}
