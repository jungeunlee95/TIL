package kr.co.mlec.day07.homework;

import java.util.Scanner;

public class HWMain01 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("���ڿ� �Է� : ");
		String strData = scan.nextLine();
		System.out.print("�����Է� : ");
		char ch = scan.nextLine().charAt(0);

		int num = StringUtil.checkChar(strData, ch);
		System.out.println("[" + strData + "] �� \'" + ch + "\'�� " + num + "�� �ֽ��ϴ�.");
		
		String str = StringUtil.removeChar(strData, ch);
		System.out.println("��� : " + str);
		
		scan.close();
	}

}
