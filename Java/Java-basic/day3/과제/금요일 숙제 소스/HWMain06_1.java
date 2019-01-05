package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
6. ���۴�, ������� �Է¹޾� �������� ���
   ���۴� : 6  8
   ����� : 8  6
   
   *** 6�� ***
   6 * 1 = 6
   
   *** 7�� ***
   ...
   8 * 9 = 72   
*/

public class HWMain06_1 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		System.out.print("���۴� : ");
		int start = scan.nextInt();
		System.out.print("����� : ");
		int end = scan.nextInt();
		
		if(start> end) {   //start ���� �� ũ�ٸ� end ���� ��ü
			int a = start;
			start = end;
			end = a;
		}
		
		for(int i=start; i<=end; i++) {
			System.out.println("*** " + i + "�� ***");
			for(int j=1; j<10; j++) {
				System.out.println(i + " * " + j + " = " + i * j);
			}
			System.out.println();
		}
		
		scan.close();
	}
	
	
	

}
