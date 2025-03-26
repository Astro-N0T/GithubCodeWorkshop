#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define ARRAY_SIZE 100000000  // Large array size
#define NUM_THREADS 4         // Number of threads

long long global_sum = 0;     // Shared global sum
pthread_mutex_t mutex;        // Mutex for thread-safe access

// Array to sum
int* array;

// Function executed by each thread
void* thread_sum(void* arg) {
    int thread_id = *(int*)arg;
    long long local_sum = 0;

    // Calculate the start and end indices for this thread
    int start = thread_id * (ARRAY_SIZE / NUM_THREADS);
    int end = (thread_id + 1) * (ARRAY_SIZE / NUM_THREADS);

    // Sum the portion of the array assigned to this thread
    for (int i = start; i < end; i++) {
        local_sum += array[i];
    }

    // Add local sum to the global sum safely
    pthread_mutex_lock(&mutex);
    global_sum += local_sum;
    pthread_mutex_unlock(&mutex);

    pthread_exit(NULL);
}

int main() {
    // Allocate and populate the array
    array = malloc(ARRAY_SIZE * sizeof(int));
    for (int i = 0; i < ARRAY_SIZE; i++) {
        array[i] = 1;  // For simplicity, every element is 1
    }

    // Measure time for single-threaded summation
    printf("Starting single-threaded summation...\n");
    clock_t start_time = clock();
    long long single_thread_sum = 0;
    for (int i = 0; i < ARRAY_SIZE; i++) {
        single_thread_sum += array[i];
    }
    clock_t end_time = clock();
    printf("Single-threaded sum: %lld\n", single_thread_sum);
    printf("Time taken (single-threaded): %.3f seconds\n\n",
           (double)(end_time - start_time) / CLOCKS_PER_SEC);

    // Measure time for multi-threaded summation
    printf("Starting multi-threaded summation...\n");
    pthread_t threads[NUM_THREADS];
    int thread_ids[NUM_THREADS];

    // Initialize the mutex
    pthread_mutex_init(&mutex, NULL);

    start_time = clock();
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i;
        pthread_create(&threads[i], NULL, thread_sum, &thread_ids[i]);
    }

    // Wait for all threads to finish
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
    end_time = clock();

    printf("Multi-threaded sum: %lld\n", global_sum);
    printf("Time taken (multi-threaded): %.3f seconds\n",
           (double)(end_time - start_time) / CLOCKS_PER_SEC);

    // Cleanup
    pthread_mutex_destroy(&mutex);
    free(array);

    return 0;
}
