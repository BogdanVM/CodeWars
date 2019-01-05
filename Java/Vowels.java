public class Vowels {

  public static int getCount(String str) {
    int vowelsCount = 0;
    
    String vowels = "aeiou"; // store all the vowels in a string
    for (int i = 0; i < str.length(); ++i) {
        /* Iterate through all the chars of the string and check if the current char is found in the vowels string */
        if (vowels.indexOf(str.charAt(i)) >= 0) {
            vowelsCount++;
        }
    }
    
    return vowelsCount;
  }

}