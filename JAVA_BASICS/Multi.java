//BOJ #2588 °ö¼À
//ÀÔÃâ·Â°ú ¿¬»êÀÚ

package basics;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Multi {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        
		int num4 = b%10;
		int num5 = (b%100)/10;
		int num6 = b/100;
		
		System.out.println(a*num4);
		System.out.println(a*num5);
		System.out.println(a*num6);
		System.out.println(a*b);
	}
}
