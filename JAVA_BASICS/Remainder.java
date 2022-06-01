// BOJ#3052 나머지
// 1차원배열 - contains(), add()

package basics;

import java.io.*;
import java.util.*;

public class Remainder{
	public static void main(String[] arg) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = "";
		
		int[] nums = new int[10];
		ArrayList remainders = new ArrayList();
		int temp = 0;	//나머지를 임시로 저장할 변수
		int result = 0;	//결과 값을 저장할 변수
		
		for(int i=0;i<10;i++) {
			 nums[i] = Integer.parseInt(br.readLine());
			 temp = nums[i]%42;
			 
			//remainder 배열에 이번 나머지값이 있는지 확인
			 if(remainders.contains(temp) == false) { 	
				 remainders.add(temp);
				 result+=1;
			 }
		}
		
		System.out.println(result);
	}
}
