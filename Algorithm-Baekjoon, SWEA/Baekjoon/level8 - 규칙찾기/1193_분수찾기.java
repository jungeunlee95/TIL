/*
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을
1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로
1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

출력
첫째 줄에 분수를 출력한다.
*/

import java.util.Scanner;

public class Main {
	    private static String getFrac(int n) {
	        int lv = 1;
	        int lv_size = 1;
	        int total = 1;
	        int offset = 1;
	        int a = 1;
	        int b = 1;
	        while( total < n ) {
	            lv_size++;
	            offset = n - total;
	            if( lv%2 == 0 ) {
	                a = lv_size - offset + 1;
	                b = offset;
	            }
	            else {
	                a = offset;
	                b = lv_size - offset + 1;
	            }
	            total += lv_size;
	            lv++;
	        }
	        return String.valueOf(a)+"/"+String.valueOf(b);
	    }
	    public static void main(String args[]) {
	        Scanner sc = new Scanner(System.in);
	        int n = sc.nextInt();
	        System.out.println( getFrac(n) );
	    }

}
