int thirdMax(int* nums, int numsSize) {
     for (int i = 0; i < numsSize; i++) {
        int min_index = i;

        for (int j = i + 1; j < numsSize; j++) {
            if (nums[j] < nums[min_index]) {
                min_index = j;
            }
        }

        int temp = nums[i];
        nums[i] = nums[min_index];
        nums[min_index] = temp;
    }

    int l = 0;

    for (int i = 0; i < numsSize; i++) {
        if (l == 0 || nums[i] != nums[l - 1]) {
            nums[l] = nums[i];
            l++;
        }
    }

    if (l < 3) {
        return nums[l - 1];
    }

    return nums[l - 3];
}
