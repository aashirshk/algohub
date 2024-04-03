void selectionSort(List<int> numbers) {
  // [10, 11, 5, 2, 4, 6, 0, 1]

  int temp;

  for (int i = 0; i < numbers.length; i++) {
    int currentMinElementIndex = i;
    for (int j = i + 1; j < numbers.length; j++) {
      if (numbers[j] < numbers[currentMinElementIndex]) {
        currentMinElementIndex = j;
      }
    }
    temp = numbers[i];
    numbers[i] = numbers[currentMinElementIndex];
    numbers[currentMinElementIndex] = temp;
  }
}
