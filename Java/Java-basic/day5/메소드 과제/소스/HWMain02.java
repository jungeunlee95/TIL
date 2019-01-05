package kr.co.mlec.day06.homework;

import java.util.Scanner;

public class HWMain02 {

	public static void main(String[] args) {
		
		StringUtil sutil = new StringUtil();
		Scanner scan = new Scanner(System.in);
		
		System.out.print("문자입력 : ");
		char ch = scan.nextLine().charAt(0);
		System.out.println(ch + "는 대문자이다 : " + sutil.isUpperChar(ch));
		
		System.out.print("문자입력 : ");
		ch = scan.nextLine().charAt(0);
		System.out.println(ch + "는 소문자이다 : " + sutil.isLowerChar(ch));
		
		System.out.print("숫자입력 : ");
		int num1 = scan.nextInt();
		System.out.print("숫자입력 : ");
		int num2 = scan.nextInt();
		System.out.println("큰 수는 : " + sutil.max(num1, num2));
		System.out.println("작은 수는 : " + sutil.min(num1, num2));
		
		scan.nextLine();
		
		System.out.print("문자열 입력 : ");
		String str = scan.nextLine();
		System.out.println("< REVERSE >");
		System.out.println(sutil.reversString(str));
		
		System.out.println("<  TO LOWER >");
		System.out.println(sutil.toLowerString(str));
		
		System.out.println("<  TO UPPER >");
		System.out.println(sutil.toUpperString(str));
		
		scan.close();
	}

}
