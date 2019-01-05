package kr.co.mlec.day07.homework;
public class StringUtil {

	// 하나의 문자를 입력받아 해당 문자가 대문자이면 true 를 반환하는 isUpperChar( char c ) 메소드를 작성하시오
	boolean isUpperChar(char c) {
		if (c >= 'A' && c <= 'Z')
			return true;
		else
			return false;
	}

	// 하나의 문자를 입력받아 해당 문자가 소문자이면 true를 반환하는 isLowerChar(char c) 메 소드를 작성하시오
	boolean isLowerChar(char c) {
		if (c >= 'a' && c <= 'z')
			return true;
		return false;
	}

	// 두개의 숫자를 입력받아 큰수를 반환하는 max( int i, int j) 메소드를 작성하시오
	int max(int i, int j) {
		return i > j ? i : j;
	}
	
	//두개의 숫자를 입력받아 작은수를 반환하는 min(int i, int j) 메소드를 작성하시오
	int min(int i, int j) {
		return i < j ? i : j;
	}
	
	//문자열을 입력받아 거꾸로 변경하는 reverseString( String str ) 메소드를 작성하시오 
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
	
	//문자열을 입력받아 대문자로 변경하는 toUpperString( String str ) 메소드를 작성하시오
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
	
	//문자열을 입력받아 소문자로 변경하는 toLowerString( String str ) 메소드를 작성하시오
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
	/*문자열에서 문자를 찾는 문제입니다. 입력값에 따라 다음과 같은 출력이 나 오도록 해당 char 의 개수를 리턴하는 checkChar 메소드를 작성하시오. 
	 * 
	 * public static int checkChar(String strData, char ch) 
	 * - 문자열의 각 내용들을 비교하여 입력 받는 char c의 값과 동일한 char 의 개수를 리턴 한다. 
	 * - 대소문자 구별하여 비교한다. 
	 * 
	 * <<처리 결과>> 
	 	입력 스트링 : String strData = "Hello World Java"; 
	 	a. ch = ’o’ 인 경우   =>  2 리턴  
	 	b. ch = ’W’ 인 경우  =>  1 리턴
	 */
	public static int checkChar(String strData, char ch) {
		int num = 0;
		for(int i=0; i<strData.length(); i++) {
			if(ch == strData.charAt(i)) num++;
		}
		
		return num;
	}
	/*
	 * 다음은 주어진 문자열에서 특정 문자를 제거하는 문제입니다.  
	 * public static String removeChar(String oriStr, char delChar) 
	 *  - 문자열 (oriStr)의 내용 중 주어진 문자(delChar)를 삭제한다. 
	 *  - 삭제된 내용으로 문자열의 내용을 변경한다. 
	 *  
	 *  <<처리 결과>> 
 		입력 스트링 : String oriStr = "Hello World Java" 
 		a.  delChar = 'l' 인 경우  =>  Heo Word Java  리턴 
 		b.  delChar = 'o' 인 경우  =>  Hell Wrld Java   리턴
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