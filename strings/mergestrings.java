package strings;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder ns = new StringBuilder(); //new string
        int i = 0;
        
        // Merge the characters alternately from both words
        while (i < word1.length() && i < word2.length()) {
            ns.append(word1.charAt(i));
            ns.append(word2.charAt(i));
            i++;
        }
        
        // If there are remaining characters in word1, append them
        while (i < word1.length()) {
            ns.append(word1.charAt(i));
            i++;
        }
        
        // If there are remaining characters in word2, append them
        while (i < word2.length()) {
            ns.append(word2.charAt(i));
            i++;
        }
        
        // Convert the StringBuilder to a String and return it
        return ns.toString();    
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String word1 = "abc";
        String word2 = "pqrst";
        System.out.println("Merged string is: " + solution.mergeAlternately(word1, word2));
    }
}
