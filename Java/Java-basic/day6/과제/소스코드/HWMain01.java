package kr.co.mlec.day07.homework;

import java.util.Scanner;

public class HWMain01 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("문자열 입력 : ");
		String strData = scan.nextLine();
		System.out.print("문자입력 : ");
		char ch = scan.nextLine().charAt(0);

		int num = StringUtil.checkChar(strData, ch);
		System.out.println("[" + strData + "] 에 \'" + ch + "\'가 " + num + "개 있습니다.");
		
		String str = StringUtil.removeChar(strData, ch);
		System.out.println("결과 : " + str);
		
		scan.close();
	}

}
