// BOJ#10871 X보다 작은 수
// 반복문

package basics;

import java.io.*;

public class XsmallerNum {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input1 = br.readLine();
		String input2 = br.readLine();
		
		String[] nx = input1.split(" "); //n과 x
		int n = Integer.parseInt(nx[0]);
		int x = Integer.parseInt(nx[1]);
		
		String[] nums = input2.split(" ");
		int[] seq = new int[n];
		for(int i=0;i<n;i++) {
			seq[i] = Integer.parseInt(nums[i]);
			if (seq[i]<x) System.out.printf("%d ",seq[i]);
		}
		
		
	}
}
