package kr.co.mlec.day04.homework;

import java.util.Scanner;

/*
	11. �л� 5���� ������ �Է¹޾� ������ ���� ����ϴ� �ڵ带 �Է�
   1's ���� : 84
   2's ���� : 1000 
   3's ���� : -45 
   4's ���� : 99 
   5's ���� : 56
   
   < PRINT >
      ��ȣ    ����   ����
    1   84   B
    2   ERROR!!!
    3   ERROR!!!
    4   99   A
    5   56   F
   5ȸ �Է� �� [2]ȸ �����߻� 
      ���� : 239��
      ��� : 47.80��
  
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
			System.out.print(i+1+"'s ���� : ");
			score[i] = scan.nextInt();  // ���� �Է�
			
			if(score[i]<0 || score[i]>100) {
				cnt++;
				score[i] = -1;			//�Ŀ� �迭�� ����ִ� ���� Error���� �ƴ����� �Ǵ��ϱ� ���� , -1�̸� Error
			}else {
				switch(score[i]/10) {   //Error�� �ƴ϶�� ���� ���
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
		System.out.println("�л�  ����  ����");
		
		for(int i=0; i<score.length; i++) {
			if(score[i] == -1) System.out.println(" " + (i+1) + " ERROR!!!");   //�迭���� -1�̸� Error ���
			else System.out.println(" " + (i+1) +"  " + score[i] + "  " + grade[i]);
		}
		
		System.out.println(score.length + "ȸ �Է� ��"+"["+cnt+"]ȸ �����߻� ");
		
		int sum = 0;
		for(int i=0; i<score.length; i++) {
			if(score[i] != -1)   sum+=score[i];   //Error�� �ƴ� �κи� �հ�
		}
		
		System.out.println("���� : " + sum);
		System.out.println("��� : " + (double)sum/(score.length-cnt));   //Error Ƚ���� �����Ͽ� ���
		
	}

}
