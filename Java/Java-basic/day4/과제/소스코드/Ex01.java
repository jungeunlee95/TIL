package day05;

import java.util.Scanner;

class Icecream {
	String name;	// 아이스크림명
	int price;		// 아이스크림가격
}

public class Ex01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("아이스크림 몇개 구입할래? ");
		int count = sc.nextInt();

		Icecream[] icecream = new Icecream[count];
		
		for(int i=0; i<count; i++) {
			System.out.println("*** " + (i+1) +"번째 아이스크림 정보 입력 ***");
			
			icecream[i] = new Icecream();
			
			System.out.print("아이스크림명: ");
			icecream[i].name = sc.next();
			
			System.out.print("아이스크림가격: ");
			icecream[i].price = sc.nextInt();
			
			System.out.println();
		}
		
		System.out.println("< 아이스크림 구매 정보 >");
		System.out.println("번호      아이스크림명     아이스크림가격");
		for(int i=0; i<count; i++) {
			System.out.println("  " + (i+1) + "     " + icecream[i].name + "             " + icecream[i].price);
		}
	}

}
