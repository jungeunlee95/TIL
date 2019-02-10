/*
다솜이는 은진이의 옆집에 새로 이사왔다. 
다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 
한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 
(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. 
N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 필요한 세트의 개수를 출력한다.
 */
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		// 각 숫자별(0~9) 사용 횟수를 저장하는 배열을 생성한다.
		int[] number = new int[10];

		String roomNumber = scanner.next();

		roomNumber = roomNumber.replace('6', '9');

		int index;
		for (char ch : roomNumber.toCharArray()) {
			index = (int) ch - 48;

			// 숫자 사용 횟수를 증가시킨다.
			number[index] += 1;
		}

		int maxUseCount = -1;
		int useCount = 0;

		for (int i = 0; i < 10; i++) {
			// 숫자 9의 경우 6과 함께 카운트가 되었으므로 2로 나누어서 반올림한다.
			if (i == 9) {
				useCount = (int) Math.round(number[9] / 2.0);
			} else {
				useCount = number[i];
			}

			if (useCount > maxUseCount) {
				maxUseCount = useCount;
			}
		}

		System.out.println(maxUseCount);

		scanner.close();
	}
}