package Day2Homework;

import java.util.Scanner;

/*
 *1�޷��� ���� 1,092.50�� �Դϴ�. 
 *ȭ�鿡�� �޷��� �Է� �޾� ��ȭ�� �����ִ� ���α׷��� �ۼ��ϼ���

�޷��� �Է��ϼ��� ? 10
��ȭ : 1092.50��

 */
public class Number5 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.print("�޷��� �Է��ϼ��� : ");
		int usd = sc.nextInt();
		
		double krw;
		krw = 1092.50;
		
		System.out.print("��ȭ : " + (usd*krw) + "��");
		
		
		
		
	}

}
