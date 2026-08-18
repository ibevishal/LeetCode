void sortColors(int* nums, int numsSize) {
    int min_index;

    for (int i = 0; i < numsSize; i++) {
        min_index = i;

        for (int j = i + 1; j < numsSize; j++) {
            if (nums[j] < nums[min_index]) {
                min_index = j;
            }
        }

        int temp = nums[i];
        nums[i] = nums[min_index];
        nums[min_index] = temp;
    }
}