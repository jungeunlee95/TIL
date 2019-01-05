package kr.co.mlec.day06.homework;

import java.util.Scanner;

public class HWMain02 {

	public static void main(String[] args) {
		
		StringUtil sutil = new StringUtil();
		Scanner scan = new Scanner(System.in);
		
		System.out.print("�����Է� : ");
		char ch = scan.nextLine().charAt(0);
		System.out.println(ch + "�� �빮���̴� : " + sutil.isUpperChar(ch));
		
		System.out.print("�����Է� : ");
		ch = scan.nextLine().charAt(0);
		System.out.println(ch + "�� �ҹ����̴� : " + sutil.isLowerChar(ch));
		
		System.out.print("�����Է� : ");
		int num1 = scan.nextInt();
		System.out.print("�����Է� : ");
		int num2 = scan.nextInt();
		System.out.println("ū ���� : " + sutil.max(num1, num2));
		System.out.println("���� ���� : " + sutil.min(num1, num2));
		
		scan.nextLine();
		
		System.out.print("���ڿ� �Է� : ");
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
