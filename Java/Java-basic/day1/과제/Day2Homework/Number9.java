package Day2Homework;
/*
 *������ ����� ���̴� ���α׷��� �ۼ�
�����ϰ� �ִ� å�Ǽ� : -34
�߸��Է��߽��ϴ�

�����ϰ� �ִ� å�Ǽ� : 0
�����ϰ� �ִ� å ����

�����ϰ� �ִ� å�Ǽ� : 1
1 book

�����ϰ� �ִ� å�Ǽ� : 12
12 books

 */

import java.util.Scanner;

public class Number9 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
	    System.out.print("�����ϰ� �ִ� å �Ǽ� �Է� : ");
	    int book = sc.nextInt();
		
	    if(book == 0) {
	    	System.out.println("�����ϰ� �ִ� å ����");
	    } else if (book == 1) {
	    	System.out.println(book + " book");
        } else if (book >0){
        	System.out.println(book + " books");
        } else {
        	System.out.println("�߸� �Է� �߽��ϴ�.");
        }
		
	 
	    
	}

}
