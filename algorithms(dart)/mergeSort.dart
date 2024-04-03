void mergeSort(List<int> numbers, int start, int end) {
  if (start < end) {
    int mid = (start + end) ~/ 2;
    mergeSort(numbers, start, mid);
    mergeSort(numbers, mid + 1, end);
    merge(numbers, start, end, mid);
  }
}

void merge(List<int> numbers, int start, int end, int mid) {
  List<int> temp = List.filled(end-start+1, 0);
  int k = 0;
  int i = start;
  int j = mid + 1;

  while(i<=mid && j<=end){
    if(numbers[i]<numbers[j]){
      temp[k] = numbers[i];
      i++;
      k++;
    }
    else{
      temp[k] = numbers[j];
      j++;
      k++;
    }
  }
  while(i<=mid){
    temp[k] = numbers[i];
    i++;
    k++;
  }
  while(j<=end){
    temp[k] = numbers[j];
    j++;
    k++;
  }

  k = 0;

  for(int l = start; l<end+1; l++){
    numbers[l] = temp[k];
    k++;
  }
}
