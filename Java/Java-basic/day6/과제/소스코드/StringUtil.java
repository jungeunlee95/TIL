package kr.co.mlec.day07.homework;
public class StringUtil {

	// �ϳ��� ���ڸ� �Է¹޾� �ش� ���ڰ� �빮���̸� true �� ��ȯ�ϴ� isUpperChar( char c ) �޼ҵ带 �ۼ��Ͻÿ�
	boolean isUpperChar(char c) {
		if (c >= 'A' && c <= 'Z')
			return true;
		else
			return false;
	}

	// �ϳ��� ���ڸ� �Է¹޾� �ش� ���ڰ� �ҹ����̸� true�� ��ȯ�ϴ� isLowerChar(char c) �� �ҵ带 �ۼ��Ͻÿ�
	boolean isLowerChar(char c) {
		if (c >= 'a' && c <= 'z')
			return true;
		return false;
	}

	// �ΰ��� ���ڸ� �Է¹޾� ū���� ��ȯ�ϴ� max( int i, int j) �޼ҵ带 �ۼ��Ͻÿ�
	int max(int i, int j) {
		return i > j ? i : j;
	}
	
	//�ΰ��� ���ڸ� �Է¹޾� �������� ��ȯ�ϴ� min(int i, int j) �޼ҵ带 �ۼ��Ͻÿ�
	int min(int i, int j) {
		return i < j ? i : j;
	}
	
	//���ڿ��� �Է¹޾� �Ųٷ� �����ϴ� reverseString( String str ) �޼ҵ带 �ۼ��Ͻÿ� 
	String reversString(String str) {
		char[] ch = new char[str.length()];
		/*for(int i = str.length()-1; i>=0; i--) {
			ch[i] = str.charAt(str.length()-i-1);
		}*/
		for(int i = str.length()-1, j=0; i>=0; i--, j++) {
			ch[j] = str.charAt(i);
		}
	
		return new String(ch);
	}
	
	//���ڿ��� �Է¹޾� �빮�ڷ� �����ϴ� toUpperString( String str ) �޼ҵ带 �ۼ��Ͻÿ�
	String toUpperString(String str) {
		char[] ch = new char[str.length()];
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i)>='a' && str.charAt(i)<='z') {
				ch[i] = (char)(str.charAt(i) - 32);
			}else {
				ch[i] = str.charAt(i);
			}
		}
		return String.valueOf(ch);    // == return new String(ch);
	}
	
	//���ڿ��� �Է¹޾� �ҹ��ڷ� �����ϴ� toLowerString( String str ) �޼ҵ带 �ۼ��Ͻÿ�
	String toLowerString(String str) {
		char[] ch = new char[str.length()];
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i)>='A' && str.charAt(i)<='Z') {
				ch[i] = (char)(str.charAt(i) + 32);
			}else {
				ch[i] = str.charAt(i);
			}
		}
		
		return new String(ch);
	}
	/*���ڿ����� ���ڸ� ã�� �����Դϴ�. �Է°��� ���� ������ ���� ����� �� ������ �ش� char �� ������ �����ϴ� checkChar �޼ҵ带 �ۼ��Ͻÿ�. 
	 * 
	 * public static int checkChar(String strData, char ch) 
	 * - ���ڿ��� �� ������� ���Ͽ� �Է� �޴� char c�� ���� ������ char �� ������ ���� �Ѵ�. 
	 * - ��ҹ��� �����Ͽ� ���Ѵ�. 
	 * 
	 * <<ó�� ���>> 
	 	�Է� ��Ʈ�� : String strData = "Hello World Java"; 
	 	a. ch = ��o�� �� ���   =>  2 ����  
	 	b. ch = ��W�� �� ���  =>  1 ����
	 */
	public static int checkChar(String strData, char ch) {
		int num = 0;
		for(int i=0; i<strData.length(); i++) {
			if(ch == strData.charAt(i)) num++;
		}
		
		return num;
	}
	/*
	 * ������ �־��� ���ڿ����� Ư�� ���ڸ� �����ϴ� �����Դϴ�.  
	 * public static String removeChar(String oriStr, char delChar) 
	 *  - ���ڿ� (oriStr)�� ���� �� �־��� ����(delChar)�� �����Ѵ�. 
	 *  - ������ �������� ���ڿ��� ������ �����Ѵ�. 
	 *  
	 *  <<ó�� ���>> 
 		�Է� ��Ʈ�� : String oriStr = "Hello World Java" 
 		a.  delChar = 'l' �� ���  =>  Heo Word Java  ���� 
 		b.  delChar = 'o' �� ���  =>  Hell Wrld Java   ����
	 */
	 public static String removeChar(String oriStr, char delChar) {
		 char[] chars = new char[oriStr.length()];
		 for(int i=0, j=0; i<oriStr.length(); i++) {
			 if(oriStr.charAt(i) != delChar) {
				 chars[j] = oriStr.charAt(i); 
				 j++;
			 }
		 }
		 
		 return new String(chars);
	 }
	

}