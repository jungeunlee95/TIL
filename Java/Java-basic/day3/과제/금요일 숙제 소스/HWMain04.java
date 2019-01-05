package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
4. 단을 입력받아 해당 구구단을 출력
   2 - 9 : 6
   
   *** 6단 ***
   6 * 1 = 6
   6 * 2 = 12
   ...
   6 * 9 = 54

*/

public class HWMain04 {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);

		System.out.print("2 - 9 : ");
		int dan = scan.nextInt();

		System.out.println("*** " + dan + "단 ***");
		for (int i = 1; i < 10; i++) {
			System.out.println(dan + " * " + i + " = " + dan * i);
		}
		
		scan.close();
	}

}
