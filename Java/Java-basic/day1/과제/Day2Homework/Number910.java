package Day2Homework;

import java.util.Scanner;

/*
 *���� 3���� �Է¹޾� ū������ ������ ������ ����ϴ� �ڵ带 �ۼ�
ù��° ���� : 12
�ι�° ���� : 26
����° ���� : 16
26  16  12

 */
public class Number910 {
public static void main(String[] args) {
		
		int a, b, c ;
		
		Scanner sc = new Scanner(System.in);
	    System.out.print("ù��° ������ �Է��ϼ��� : ");
	    a = sc.nextInt();
	    System.out.print("�ι�° ������ �Է��ϼ��� : ");
	    b = sc.nextInt();
	    System.out.print("����° ������ �Է��ϼ��� : ");
	    c = sc.nextInt();
	    /*
	     * a>b>c
	     * a>c>b
	     * b>a>c
	     * b>c>a
	     * c>a>b
	     * c>b>a
	     */
	    
	    if(a>b & b>c) {
	    	System.out.printf("ū�� ������ ���� ��� : %d %d %d\n", a,b,c);
	    } else if (a>c & c>b) {
	    	System.out.printf("ū�� ������ ���� ��� : %d %d %d\n", a,c,b);
	    } else if (b>a & a>c) {
	    	System.out.printf("ū�� ������ ���� ��� : %d %d %d\n", b,a,c);
	    } else if (b>c & b>a) {
	    	System.out.printf("ū�� ������ ���� ��� : %d %d %d\n", b,c,a);
	    } else if (c>a & a>b) {
	    	System.out.printf("ū�� ������ ���� ��� : %d %d %d\n", c,a,b);
	    } else {
	    	System.out.printf("ū�� ������ ���� ��� : %d %d %d\n", c,b,a);
	    }
	    
	    }

}
