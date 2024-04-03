import 'bubbleSort.dart';
import 'selectionSort.dart';
import 'insertionSort.dart';
import 'mergeSort.dart';

void main() {
  List<int> numbers = [10, 11, 5, 2, 4, 6, 0, 1];
  // bubbleSort(numbers);
  // print(numbers);
  mergeSort(numbers, 0, numbers.length-1);
  print(numbers);
}
