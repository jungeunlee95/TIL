package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
8. 다음의 결과를 보이는 프로그램 작성

   num1 : 12
   num2 : 9
   num2 : 15
   num2 : 6
   num3 : 94
   num4 : 6
   num5 : 11
   num5 : 12
   
   < PRINT >
   12  6  94  6  12

*/

public class HWMain08 {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		int[] num = new int[5];
		int cnt = 1;
		do {
			System.out.print("num" + cnt + " : ");
			num[cnt-1] = scan.nextInt();
			System.out.println(cnt);
			if (num[cnt-1] % 2 == 0) {
				if (cnt == 5)
					break;
				cnt++;
			}
		} while (true);

		System.out.println("< PRINT >");

		for (int i = 0; i < num.length; i++) {
			System.out.print(num[i] + " ");
		}

		scan.close();
	}

}
