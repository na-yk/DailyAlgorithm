//BOJ#2577 숫자의 개수
//1차원 배열

package basics;

import java.io.*;
import java.util.*;

public class HowManyNums {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] input = new int[3];
		int cal = 1;
		
		for(int i=0;i<3;i++) {
			input[i] = Integer.parseInt(br.readLine());
			cal*=input[i];
		}
		
		int[] result = new int[10];
		int index = 0;
		for(int i=0;i<Integer.toString(cal).length();i++) {
			index = Integer.toString(cal).charAt(i)-'0';
			result[index]+=1;
		}
		for(int i=0;i<10;i++) {
			System.out.println(result[i]);
		}
	}

}
