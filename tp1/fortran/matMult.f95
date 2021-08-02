program matMult
    implicit none

    ! Declaring variables that will be received in the inputs
    character(len=32) :: arg   
    integer :: n, multType, i, j
    real*8 :: startTime, endTime, sum
    real*8, dimension(:,:), allocatable :: A
    real*8, dimension(:), allocatable :: x, b

    ! Getting the first argument which is the size of the A (n), n int, max 15 digits
    call getarg(1, arg)    
    read(arg,"(I15)") n

    !Check which function will run # 1: external_i and 2: external_j, multType int, max 1 digit
    call getarg(2, arg)    
    read(arg,"(I1)") multType

    ! Allocating variables
    allocate(A(n, n))
    allocate(x(n))
    allocate(b(n))

    ! Random seed to generate pseudorandom matrices
    call random_seed()

    call random_number(A)
    call random_number(x)

    if (multType == 1) then !external_i

        call cpu_time(startTime) 
        do i = 1, n
            sum = 0
            do j = 1, n
                b(i)= b(i) + A(i,j)*x(j)
            end do
            b(i) = sum
        end do 
        call cpu_time(endTime)


    else if (multType == 2) then !external_j

        call cpu_time(startTime) 
        do i = 1,n
            b(i) = 0
        end do

        do j = 1, n
            do i = 1, n
                b(i) = b(i) + A(i,j)*x(j)
            end do
        end do 
        call cpu_time(endTime) 

    else
        print *, "ERROR!"
        print *, "To run it, there are two arguments:"
        print *, "          arg[1] = size of A"
        print *, "          arg[2]: 1 to do an external_i product or 2 to do an external_j product"
        CALL EXIT(0)
    end if

    print *, n, ";", (endTime - startTime)

    !Deallocating variables
    deallocate(A)
    deallocate(x)
    deallocate(b)
    
end program matMult       