package Day2Homework;

import java.util.Scanner;

/*
 *1달러는 현재 1,092.50원 입니다. 
 *화면에서 달러를 입력 받아 원화로 보여주는 프로그램을 작성하세요

달러를 입력하세요 ? 10
원화 : 1092.50원

 */
public class Number5 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("달러를 입력하세요 : ");
		int usd = sc.nextInt();
		
		double krw;
		krw = 1092.50;
		
		System.out.print("원화 : " + (usd*krw) + "원");
		
		
		
		
	}

}
