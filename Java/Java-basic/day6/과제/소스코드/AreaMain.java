package kr.co.mlec.day07.homework;

import java.util.Random;

/*
 * - ������ ���� ������ ������ ǥ���� ������ ���ڸ� �����մϴ�.(1 ~ 4)  => Random
 *    ��> 1-���簢��, 2-���簢��, 3-�ﰢ��, 4-�� 
 * - ������ ���ڿ� ����  
 * 	1, 4���� ���� ������ ������ ���� ���� ���ڸ� 1�� �����մϴ�. 
 *  2, 3���� ���� ������ ������ ���� ���� ���ڸ� 2�� �����մϴ�.   
 *  => Random & switch
 *  
 *  ������ ���� ���� ���ڱ��� �����Ǿ��ٸ� ������ ������ ������ ���ϴ� Ŭ������ ȣ���մϴ�
 */
public class AreaMain {

	public static void main(String[] args) {
		Random rand = new Random();
		int num = rand.nextInt(4) + 1;
		int num2 = rand.nextInt(10) + 1;
		int num3;
		
		System.out.println(num + "  " + num2);
		
		switch (num) {
		case 1:
			SquareArea s = new SquareArea(num2);
			System.out.println("���簢���� ���� : " + s.area());
			break;
		case 2:
			num3 = rand.nextInt(10) + 1;
			System.out.println(num3);
			Area a = new Area(num2, num3);
			System.out.println("���簢���� ���� : " + a.area());
			break;
		case 3:
			num3 = rand.nextInt(10) + 1;
			TriArea t = new TriArea(num2, num3);
			System.out.println("�ﰢ���� ���� : " + t.area());
			break;
		case 4:
			CircleArea c = new CircleArea(num2);
			System.out.println("���� ���� : " + c.area());
			break;

		default:

		}

	}

}
