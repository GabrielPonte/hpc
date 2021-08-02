#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ERROR_ARGUMENTS 1


int main(int argc, char *argv[])
{
    
    // Getting arguments
    int n = atoi(argv[1]);
    int multType = atoi(argv[2]);

    // Allocate resources
    clock_t start, end;
    double **A = (double **)malloc(n * sizeof(double *));
    for (unsigned i = 0; i < n; i++)
    A[i] = (double *)malloc(n * sizeof(double));
    double *x = (double *)malloc(n * sizeof(double));
    double *b = (double *)malloc(n * sizeof(double));

    // Invalid number of arguments
    if (argc != 3 || (multType != 1 && multType != 2) || n < 1){
        printf("ERROR!\n");
        printf("To run it, there are two arguments:\n");
        printf("          arg[1] = size of A\n");
        printf("          arg[2]: 1 to do an external_i product or 2 to do an external_j product\n");
        return ERROR_ARGUMENTS;
    }

    // Initializing seed
    srand(time(NULL));

    // Initialize A and x with random values between 0 and 1
    for (long long i = 0; i < n; i++){
        x[i] = (double)(rand()) / RAND_MAX;
        for (unsigned j = 0; j < n; j++)
        A[i][j] = (double)(rand()) / RAND_MAX;
    }

    if (multType == 1){ // external_i

        start = clock();
        for (long long i = 0; i < n; i++){
            double sum = 0;
            for (long long j = 0; j < n; j++)
                sum += A[i][j] * x[j];
            b[i] = sum;
        }
        end = clock();

    }else{ // external_j
         start = clock();
        for (long long i = 0; i < n; i++){
            b[i] = 0;
        }
        for (long long j = 0; j < n; j++){
            for (long long i = 0; i < n; i++){
                b[i] += A[i][j] * x[j];
            }
        }
        end = clock();
    }


    printf("%d; %.4f\n", n, ((double)(end - start)) / CLOCKS_PER_SEC);

    return 0;
}
