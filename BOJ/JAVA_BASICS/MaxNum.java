// BOJ#2562 최댓값
// 1차원 배열


package basics;

import java.io.*;

public class MaxNum {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int nums[] = new int [9];
		
		int max = 0;
		int index = 0;
		
		for(int i=0;i<9;i++) {
			nums[i] = Integer.parseInt(br.readLine());
			if (max<nums[i]) {
				max = nums[i];
				index = i+1;
			}
		}
		
		System.out.println(max);
		System.out.println(index);
	}

}
