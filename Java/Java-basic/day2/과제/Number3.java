package Day3Homework;
/*??????????????????????
 
*-------*
**-----**
***---***
****-****

*********

****-****
***---***
**-----**
*-------*

 */
public class Number3 {

	public static void main(String[] args) {
		for(int i = 1; i <= 9; i ++) {
			for(int j= 1; j<=9; j++) {
				if(i <= 4) {
					if(i+j <= 8) {
						System.out.print('*');
					}else if (i+j >= 9) {
						System.out.print('*');
					}else {
						System.out.print("-");
					}
				}
				else if (i>=6) {
					if(i-j >1 ) {
						System.out.print('*');
					}else if (i+j >= 12) {
						System.out.print('*');
					}else {
						System.out.print('-');
					}
				}else if(i = 5) {
					System.out.print('*');
				}
			}
		}System.out.println();
	

	}

}
