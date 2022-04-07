class Solution0896 {
    fun isMonotonic(nums: IntArray): Boolean {
        if (nums.size == 1) return true
        var increase = true
        var decrease = true
        for (index in 1 until nums.size) {
            increase = increase && (nums[index] >= nums[index - 1])
            decrease = decrease && (nums[index] <= nums[index - 1])
        }
        return increase || decrease
    }
}

/*
欺负简单题混了个100题
 */
