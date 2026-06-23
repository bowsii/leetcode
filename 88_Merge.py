"""Problem 88: Merge"""

int l1=m-1;
    int l2=n-1;
    int p=n+m-1;
    while(l1>=0 && l2>=0){
        if(nums1[l1]>nums2[l2]){
            nums1[p--]=nums1[l1--];
        }
        else{
            nums1[p--]=nums2[l2--];
        }
    }
    while(l2>=0){
        nums1[p--]=nums2[l2--];
    }
}
