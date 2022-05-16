// BOJ#2525 오븐시계
// 조건문


package basics;

import java.io.*;

public class Ovenclock {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int time = Integer.parseInt(br.readLine());
		
		String[] input = str.split(" ");

		int hour = Integer.parseInt(input[0]); //시
		int min = Integer.parseInt(input[1]); //분
		
		if (time/60 > 0) {
			hour = hour+(time/60);
			if(min+time%60 < 60) {
				min = min+time%60;
			}else {
				hour++;
				min = (min+time%60)%60;
			}
		}else {
			if(min+time < 60) {
				min = min+time;
			}else {
				hour++;
				min = (min+time)%60;
			}
		}
		
		if (hour >= 24) hour-=24;
		
		System.out.printf("%d %d",hour,min);
	}

}
