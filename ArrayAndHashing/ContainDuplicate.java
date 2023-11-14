import java.util.HashSet;
import java.util.Set;

class ContainDuplicate {
    /*
        217. Contains Duplicate
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

        Example 1:
        Input: nums = [1,2,3,1]
        Output: true
        Example 2:

        Input: nums = [1,2,3,4]
        Output: false
        Example 3:
        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true
        Constraints:

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
     */
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) { // O(n)
            if (set.contains(num)) { // O(1)
                return true;
            }
            set.add(num); // O(1)
        }
        return false;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,1}; // Output: true
        int[] nums2 = {1,2,3,4}; // Output: false
        int[] nums3 = {1,1,1,3,3,4,3,2,4,2}; // Output: true
        System.out.println(containsDuplicate(nums)); // O(n)
        System.out.println(containsDuplicate(nums2)); // O(n)
        System.out.println(containsDuplicate(nums3)); // O(n)
    }
}