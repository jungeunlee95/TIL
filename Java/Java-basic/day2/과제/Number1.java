package Day3Homework;

/*
             -  *  -
********* 1  0  9  0  10-i
-*******  2  1  7  1  9-i
--*****   3  2  5  2  8-i
---***    4  3  3  3  7-i
----*     5  4  1  4  6-i         

*별 개수를 0,1,2,3,4 순으로 빼줘야함 
             
 */
public class Number1 {

	public static void main(String[] args) {
		
		for(int i = 1; i <= 5; i++) {    
			for(int j = 1; j <= 10-i; j++) {  //*개수
				if(i > j) {                 //5행까지 '-' 개수가 하나씩 늘어남
					System.out.print('-');
				} else {                    //6행부터는 *개수가 하나씩 줄어야함
					System.out.print('*');
				}
				
			}
			System.out.println();
		}
	}
}