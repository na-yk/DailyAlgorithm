//BOJ #10869 사칙연산
//입출력과 사칙연산

package basics;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Arithmetic {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = "";
		str = br.readLine();
		
		String[] nums = str.split(" ");
		int a = Integer.parseInt(nums[0]);
		int b = Integer.parseInt(nums[1]);
		
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
		System.out.println(a/b); //int형 나누기 -> 몫도 무조건 정수형
		System.out.println((double)a/b); //오차 10^-9 이하
		System.out.println(a%b);
	}
}
