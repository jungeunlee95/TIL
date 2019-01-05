
package Day3Homework;
/*
 
----*         5-1
---***        6-3
--*****       7-5
-*******      8-7
*********     9-9

-*******      8-7
--*****       7-5   
---***        6-3
----*         5-1
 */

public class Number02 {

	public static void main(String[] args) {
		for(int i = 1; i <= 9; i++) {
			for(int j = 1;j<=9; j++ ) {
				if (i<=5) {                     //위의 영역
					if (i+j<=5) {
						System.out.print('-');  //윈쪽 위의 공백
					}else if (j-i >= 5) {
						System.out.print("-");  //오른 쪽 위 공백
					} else {
						System.out.print("*");  //위의 영역에서 공백 나머지는 모두 *
					}
					
				}else if (i>5) {                //아래쪽, i가 6 이상영역
					if(i-j>=5) {
						System.out.print('-');  //아래쪽 왼쪽 공백
					}else if (i+j >= 15) {
						System.out.print('-');  //아래쪽 오른쪽 공백
					}else {
						System.out.print('*');  //아래쪽 공백 나머지를 *로
					}
				}
		} System.out.println();

	}
	}
}

