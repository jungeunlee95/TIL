package day05;

import java.util.Scanner;

class Icecream {
	String name;	// ���̽�ũ����
	int price;		// ���̽�ũ������
}

public class Ex01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("���̽�ũ�� � �����ҷ�? ");
		int count = sc.nextInt();

		Icecream[] icecream = new Icecream[count];
		
		for(int i=0; i<count; i++) {
			System.out.println("*** " + (i+1) +"��° ���̽�ũ�� ���� �Է� ***");
			
			icecream[i] = new Icecream();
			
			System.out.print("���̽�ũ����: ");
			icecream[i].name = sc.next();
			
			System.out.print("���̽�ũ������: ");
			icecream[i].price = sc.nextInt();
			
			System.out.println();
		}
		
		System.out.println("< ���̽�ũ�� ���� ���� >");
		System.out.println("��ȣ      ���̽�ũ����     ���̽�ũ������");
		for(int i=0; i<count; i++) {
			System.out.println("  " + (i+1) + "     " + icecream[i].name + "             " + icecream[i].price);
		}
	}

}
