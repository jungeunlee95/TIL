package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
6. 시작단, 종료단을 입력받아 구구단을 출력
   시작단 : 6  8
   종료단 : 8  6
   
   *** 6단 ***
   6 * 1 = 6
   
   *** 7단 ***
   ...
   8 * 9 = 72   
*/

public class HWMain06_1 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		System.out.print("시작단 : ");
		int start = scan.nextInt();
		System.out.print("종료단 : ");
		int end = scan.nextInt();
		
		if(start> end) {   //start 값이 더 크다면 end 값과 교체
			int a = start;
			start = end;
			end = a;
		}
		
		for(int i=start; i<=end; i++) {
			System.out.println("*** " + i + "단 ***");
			for(int j=1; j<10; j++) {
				System.out.println(i + " * " + j + " = " + i * j);
			}
			System.out.println();
		}
		
		scan.close();
	}
	
	
	

}
