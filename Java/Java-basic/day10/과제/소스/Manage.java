package kr.co.mlec.day11.homework;

import java.util.Scanner;

public class Manage {

	public void run() {
		Board bd = new Board();
		Scanner scan = new Scanner(System.in);
		int num;
		while(true) {
			bd.print();
			num = bd.scanInt("항목 선택");
			
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
				System.out.println("시스템 종료.");
				scan.close();
				System.exit(0);
			default:
				System.out.println("다시 선택하세요.");
			}
		}
	}
}
	
