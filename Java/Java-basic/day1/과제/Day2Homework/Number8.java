package Day2Homework;

import java.util.Scanner;
//���ǰ� 30 �϶�, ���� �׼� 5040�϶� Ʋ��..��

/*
 *���ǰ��� �Է����� �� �Ž������� �Ž������� �ش��ϴ� 
 *1000��, 500��, 100��, 50��, 10���� ������ ����ϴ� �ڵ带 �ۼ�
 *
���ǰ��� �Է� : 4820
������ ���� �׼� : 10000

�Ž����� : 5180��
1000�� : 5��
 500�� : 0��
 100�� : 1��
  50�� : 1��
  10�� : 3��

 */
public class Number8 {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("���� ���� �Է��ϼ��� : ");
		int price = sc.nextInt();
		
		System.out.print("������ ���� �׼��� �Է��ϼ��� : ");
		int pay = sc.nextInt();
		
		
		int money = pay-price;
		
		System.out.println("�Ž��� �� : " + money + "��");
		System.out.println("1000�� : " + money/1000 + "��" );
		System.out.println("500�� : " + (money%1000)/500 + "��");
		System.out.println("100�� : " + (money%1000%500)/100 + "��");
		System.out.println("50�� : " + (money%1000%500%100)/50 + "��");
		System.out.println("10�� : " + (money%1000%500%100&50)/10 + "��");
		
		
		
		}
		
		
	}


