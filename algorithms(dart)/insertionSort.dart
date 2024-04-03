void insertionSort(List<int> numbers) {
  int temp;
  for (int i = 1; i < numbers.length; i++) {
    int j = i;
    while (j > 0) {
      if (numbers[j] < numbers[j - 1]) {
        temp = numbers[j];
        numbers[j] = numbers[j - 1];
        numbers[j - 1] = temp;
      }
      j--;
      // print(i);
    }
  }
}
