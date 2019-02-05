/*
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
전화를 걸고 싶은 번호가 있다면, 
숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 
돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 
다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 
시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 
더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 
 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 
시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 
단어는 2글자~15글자로 이루어져 있다.

출력
첫째 줄에 다이얼을 걸기 위해서 필요한 시간을 출력한다.
*/
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         
        String num = sc.nextLine();
        int sum=0;
         
        for(int j=0; j<num.length(); j++) {
        char value = num.charAt(j);
         
        if('A'<= value && value <='C') {
            sum = sum + 3;
        }else if('D'<= value && value <='F') {
            sum = sum + 4;
        }else if('G'<= value && value <='I') {
            sum = sum + 5;
        }else if('J'<= value && value <='L') {
            sum = sum + 6;
        }else if('M'<= value && value <='O') {
            sum = sum + 7;
        }else if('P'<= value && value <='S') {
            sum = sum + 8;
        }else if('T'<= value && value <='V') {
            sum = sum + 9;
        }else if('W'<= value && value <='Z'){
            sum = sum + 10;
        }
        }
            System.out.println(sum);       
         
    }
}

/*
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
  
public class Main {
  
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String text = br.readLine();
        char[] word = text.toCharArray();
        int totalTime = 0;
         
        int[] alpha = {3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10};
         
        for(int i=0; i<word.length; i++) {
            for(int j=65; j<=90; j++) {
                if((int)word[i] == j)
                    totalTime += alpha[j-65];
            }
        }
        System.out.println(totalTime);
         
    }
}
*/

/*
import java.util.Scanner;

import java.util.StringTokenizer;



public class Main {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);

		

		int time = 0 ;

		String input = scan.nextLine();

		

		for(int i = 0 ; i < input.length(); i ++) {

			char charIndex = input.charAt(i);

			if( charIndex >='A' && charIndex <= 'C' ) {

				time += 3;

			} else if( charIndex >='D' && charIndex <= 'F' ) {

				time += 4;

			} else if( charIndex >='G' && charIndex <= 'I' ) {

				time += 5;

			} else if( charIndex >='J' && charIndex <= 'L' ) {

				time += 6;

			} else if( charIndex >='M' && charIndex <= 'O' ) {

				time += 7;

			} else if( charIndex >='P' && charIndex <= 'S' ) {

				time += 8;

			} else if( charIndex >='T' && charIndex <= 'V' ) {

				time += 9;

			} else if( charIndex >='W' && charIndex <= 'Z' ) {

				time += 10;

			}	

		}	

		System.out.println(time);	

	}

}
*/
