package tarea3;

public class quicksort {

	public static void main(String[] args) {

		int[] data = { 1, 8, 6, 8, 9, 2, 7, 6 }; // input Array

		printSequence(data, "Array Before Quick Sort"); // Printing the
														// sequence.

		quickSortOptimized(data, 0, data.length - 1); // Sorting the array in
														// O(nlog(n))

		printSequence(data, "Array After Quick Sort"); // Printing the sequence.

	}

	private static void quickSortOptimized(int[] data, int start, int end) {
		while (start < end) {
			int pIndex = partition(data, start, end); // Get Partition Index

			if (pIndex - start < end - pIndex) // If left side is smaller in
												// size, then sort First
			{
				quickSortOptimized(data, start, pIndex - 1);
				start = pIndex + 1;
			} else {
				quickSortOptimized(data, pIndex + 1, end); // If right side is
															// smaller in size,
															// then sort First
				end = pIndex - 1;
			}
		}
	}

	private static int partition(int[] data, int start, int end) {
		int pIndex = start;
		int pValue = data[end];

		for (int i = start; i < end; i++) {
			if (data[i] <= pValue) {
				swap(data, i, pIndex++);
			}
		}
		swap(data, end, pIndex);
		return pIndex;
	}

	private static void swap(int[] data, int index1, int index2) {
		int tempValue = data[index1];
		data[index1] = data[index2];
		data[index2] = tempValue;
	}

	public static void printSequence(int[] data, String msg) { // Printing
																// Function
		System.out.println(msg);
		for (int i = 0; i < data.length; i++) {
			System.out.print(data[i] + " ");
		}
		System.out.println();
	}
}