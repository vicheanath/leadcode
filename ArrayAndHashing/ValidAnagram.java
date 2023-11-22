import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Objects;


public class ValidAnagram {
    /*
        t anagram of s meaning t is use all character of s
           Solution :
            - use 2 different has map to store s and t
                + store char as a key and count them each s & t
                + go throw both hash map it the char counter is the same it will be anagram
     */
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
        HashMap<Character,Integer> maps = new HashMap<>();
        HashMap<Character,Integer> mapt = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
            maps.put(s.charAt(i),maps.getOrDefault(s.charAt(i),0)+1);
            mapt.put(t.charAt(i),mapt.getOrDcefault(t.charAt(i),0)+1);
        }

        for (Map.Entry<Character,Integer> entry : maps.entrySet()){
            System.out.println(entry.getValue() + " " + mapt.getOrDefault(entry.getKey(), 0));
            if (!Objects.equals(entry.getValue(), mapt.getOrDefault(entry.getKey(), 0)))
                return false;
        }
        return true;
    }

    public static void main(String[] args) {



        String s = "anagram", t = "nagaram"; //Output: true
        String s2 = "rat", t2 = "car"; //Output: false

        System.out.println(isAnagram(s,t));
        System.out.println(isAnagram(s2,t2));
    }
}
