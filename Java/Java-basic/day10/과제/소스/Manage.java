package kr.co.mlec.day11.homework;

import java.util.Scanner;

public class Manage {

	public void run() {
		Board bd = new Board();
		Scanner scan = new Scanner(System.in);
		int num;
		while(true) {
			bd.print();
			num = bd.scanInt("�׸� ����");
			
			switch (num) {
			case 1:
				bd.showAll();
				break;
			case 2 :
				bd.showPost();
				break;
			case 3 :
				bd.add();
				break;
			case 4 :
				bd.rewrite();
				break;
			case 5 :
				bd.delete();
				break;
			case 0 :
				System.out.println("�ý��� ����.");
				scan.close();
				System.exit(0);
			default:
				System.out.println("�ٽ� �����ϼ���.");
			}
		}
	}
}
	
