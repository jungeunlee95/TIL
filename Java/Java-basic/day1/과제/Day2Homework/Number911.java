package Day2Homework;

import java.util.Scanner;

/*
 *���� 4���� �Է¹޾� ���� ū���� ����ϴ� �ڵ带 �ۼ�
���� 4�� �Է� : 12 56 8 34
���� ū�� : 56

 */
public class Number911 {

	public static void main(String[] args) {
		
		int a, b, c, d;
		
		Scanner sc = new Scanner(System.in);
	    System.out.print("���� �ٸ� ���� 4���� �Է��ϼ��� : ");
	    a = sc.nextInt();
	    b = sc.nextInt();
	    c = sc.nextInt();
	    d = sc.nextInt();
	    
	    if(a>b & a>c & a>d) {
	    	System.out.println("���� ū �� : " + a);
	    } else if (b>a & b>c & b>d) {
	    	System.out.println("���� ū �� : " + b);
	    } else if (c>a & c>b & c>d) {
	    	System.out.println("���� ū �� : " + c);
	    } else {
	    	System.out.println("���� ū �� : " + d);
	    }
	    
	    }
	    
		    		
	

	
  }

