package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
3. 다음의 결과를 보이는 프로그램 작성
 2 - 9사이의 정수 입력 : 5
 
 // 1단계
 <5의 배수를 제외한 정수 출력 >
 1  2  3  4  6  7  8  9  11  12 , ..., 97  98  99
 
*/
public class HWMain03_1 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		System.out.print("2 - 9 사이의 정수 입력 : ");
		int num = scan.nextInt();
		
		for(int i=1; i<=100; i++) {
			if(i%num != 0) System.out.print(i+"  ");
		}

		scan.close();
		
	}

}
