class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let result = new Array(nums.length).fill(1);

        //For calculating the product to the left
        let product = 1
        for (let i = 1; i < nums.length; i++) {
            product *= nums[i - 1];
            result[i] *= product;
        }

        //For calculating the product to the right
        product = 1

        for (let i = nums.length - 2; i >= 0; i--) {
            product *= nums[i + 1]
            result[i] *= product

        }

        return result
    }
}
