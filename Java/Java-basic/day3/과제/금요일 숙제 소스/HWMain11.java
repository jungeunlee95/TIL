package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
	11. 학생 5명의 성적을 입력받아 다음과 같이 출력하는 코드를 입력
   1's 성적 : 84
   2's 성적 : 1000 
   3's 성적 : -45 
   4's 성적 : 99 
   5's 성적 : 56
   
   < PRINT >
      번호    성적   학점
    1   84   B
    2   ERROR!!!
    3   ERROR!!!
    4   99   A
    5   56   F
   5회 입력 중 [2]회 에러발생 
      총점 : 239점
      평균 : 47.80점
  
 90 ~ 100 : A
 80 ~ 89  : B
 70 ~ 79  : C
 60 ~ 69  : D
 0 ~  59  : F  
 */

public class HWMain11 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int[] score = new int[5];
		char[] grade = new char[5];
		int cnt=0;
		
		for(int i=0; i<score.length; i++) {
			System.out.print(i+1+"'s 성적 : ");
			score[i] = scan.nextInt();  // 점수 입력
			
			if(score[i]<0 || score[i]>100) {
				cnt++;
				score[i] = -1;			//후에 배열에 들어있는 값이 Error인지 아닌지를 판단하기 위함 , -1이면 Error
			}else {
				switch(score[i]/10) {   //Error가 아니라면 학점 계산
				case 10:
				case 9:
					grade[i] = 'A';
					break;
				case 8:
					grade[i] = 'B';
					break;
				case 7:
					grade[i] = 'C';
					break;
				case 6:
					grade[i] = 'D';
					break;
				default :
					grade[i] ='F';
					
				}
			}
		}
		scan.close();
		
		System.out.println("<  PRINT  >");
		System.out.println("학생  성적  학점");
		
		for(int i=0; i<score.length; i++) {
			if(score[i] == -1) System.out.println(" " + (i+1) + " ERROR!!!");   //배열값이 -1이면 Error 출력
			else System.out.println(" " + (i+1) +"  " + score[i] + "  " + grade[i]);
		}
		
		System.out.println(score.length + "회 입력 중"+"["+cnt+"]회 에러발생 ");
		
		int sum = 0;
		for(int i=0; i<score.length; i++) {
			if(score[i] != -1)   sum+=score[i];   //Error가 아닌 부분만 합계
		}
		
		System.out.println("총점 : " + sum);
		System.out.println("평균 : " + (double)sum/(score.length-cnt));   //Error 횟수를 제외하여 평균
		
	}

}
