void bubbleSort(List<int> numbers) {
  // sort algorithm for bubble sort.
  int temp;
  for (int i = 0; i < numbers.length - 1; i++) {
    for (int j = 0; j < numbers.length - i - 1; j++) {
      if (numbers[j] > numbers[j + 1]) {
        temp = numbers[j];
        numbers[j] = numbers[j + 1];
        numbers[j + 1] = temp;
      }
    }
  }
}

