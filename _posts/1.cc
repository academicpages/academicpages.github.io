int findMaxLength(vector<int>& nums) {
      int n = nums.size();  
      vector<int> cum_count_0(n, 0);
      vector<int> cum_count_1(n, 0);
      if(nums.front() == 0)
        cum_count_0[0] = 1;
      else
        cum_count_1[0] = 1;  
      for(int i = 1; i < n; i++) {
        if(nums[i] == 0)
          cum_count_0[i] = cum_count_0[i-1] + 1;
        else
          cum_count_1[i] = cum_count_1[i-1] + 1;  
      }
      int max_length = 0;
      for(int i = 0; i < n-1; i++) {
        for(int j = i+1; j < n; j++) {
            int count0 = cum_count_0[j] - cum_count_0[i];
            if(nums[i] == 0)
              count0 = count0 + 1;
            int count1 = cum_count_1[j] - cum_count_1[i];
            if(nums[i] == 1)
              count1 = count1 + 1;
            if(count0 == count1) {
                max_length = max(max_length, j-i+1);
            }    
        }
      }
      return max_length;
    }