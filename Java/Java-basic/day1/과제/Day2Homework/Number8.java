package Day2Homework;

import java.util.Scanner;
//물건값 30 일때, 지불 액수 5040일때 틀림..ㅠ

/*
 *물건값을 입력했을 때 거스름돈과 거스름돈에 해당하는 
 *1000원, 500원, 100원, 50원, 10원의 개수를 출력하는 코드를 작성
 *
물건값을 입력 : 4820
지불한 돈의 액수 : 10000

거스름돈 : 5180원
1000원 : 5개
 500원 : 0개
 100원 : 1개
  50원 : 1개
  10원 : 3개

 */
public class Number8 {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("물건 값을 입력하세요 : ");
		int price = sc.nextInt();
		
		System.out.print("지불한 돈의 액수를 입력하세요 : ");
		int pay = sc.nextInt();
		
		
		int money = pay-price;
		
		System.out.println("거스름 돈 : " + money + "원");
		System.out.println("1000원 : " + money/1000 + "개" );
		System.out.println("500원 : " + (money%1000)/500 + "개");
		System.out.println("100원 : " + (money%1000%500)/100 + "개");
		System.out.println("50원 : " + (money%1000%500%100)/50 + "개");
		System.out.println("10원 : " + (money%1000%500%100&50)/10 + "개");
		
		
		
		}
		
		
	}


