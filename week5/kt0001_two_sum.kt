class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val diff = HashMap<Int, Int>()
        for (index in nums.indices) {
            diff[target - nums[index]] = index
        }
        for (index in nums.indices){
            if ((diff[nums[index]] != null) && (diff[nums[index]] != index)) {
                return intArrayOf(index, diff[nums[index]]!!)
            }
        }
        return intArrayOf()
    }
}

fun main() {
    val solution = Solution()
    println(solution.twoSum(nums = intArrayOf(3, 2, 4), target = 6).contentToString())
}

/*
一小步
 */