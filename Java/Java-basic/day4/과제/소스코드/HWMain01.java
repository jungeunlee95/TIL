package kr.co.mlec.day05.homework;

import java.util.Scanner;

/*
 ���̽�ũ�� � �����ҷ�? => 4(Ű���� �Է�)

*** 1��° ���̽�ũ�� ���� �Է� ***
���̽�ũ���� : ����(Ű����)
���̽�ũ������ : 1200(Ű����)

*** 2��° ���̽�ũ�� ���� �Է� ***
���̽�ũ���� : ������
���̽�ũ������ : 1500

*** 3��° ���̽�ũ�� ���� �Է� ***
���̽�ũ���� : �޷γ�
���̽�ũ������ : 1000

*** 4��° ���̽�ũ�� ���� �Է� ***
���̽�ũ���� : �ҽ���
���̽�ũ������ : 1200

 < ���̽�ũ�� ���� ���� >
��ȣ   ���̽�ũ����   ���̽�ũ������
1         ����         1200��
2
3
4
 */
public class HWMain01 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		Icecream ic = new Icecream();

		System.out.print("���̽�ũ�� ���� ���� :");
		int num = scan.nextInt();
		ic.name = new String[num];
		ic.price = new int[num];

		for (int i = 0; i < num; i++) {
			System.out.println("*** " + (i + 1) + "��° ���̽�ũ�� ���� �Է� ***");
			System.out.print("���̽�ũ���� : ");
			ic.name[i] = scan.next();
			System.out.print("���̽�ũ�� ���� : ");
			ic.price[i] = scan.nextInt();
		}
		scan.close();

		System.out.println("��ȣ\t�̸�\t����");
		for (int i = 0; i < num; i++) {
			System.out.println((i + 1) + "\t" + ic.name[i] + "\t" + ic.price[i] + "��");
		}

	}

}

class Icecream {
	String name[];
	int price[];
}
