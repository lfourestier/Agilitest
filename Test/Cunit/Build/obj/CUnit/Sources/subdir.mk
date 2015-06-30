################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../CUnit/Sources/Automated.c \
../CUnit/Sources/Basic.c \
../CUnit/Sources/CUError.c \
../CUnit/Sources/Console.c \
../CUnit/Sources/MyMem.c \
../CUnit/Sources/TestDB.c \
../CUnit/Sources/TestRun.c \
../CUnit/Sources/Util.c 

OBJS += \
./obj/CUnit/Sources/Automated.o \
./obj/CUnit/Sources/Basic.o \
./obj/CUnit/Sources/CUError.o \
./obj/CUnit/Sources/Console.o \
./obj/CUnit/Sources/MyMem.o \
./obj/CUnit/Sources/TestDB.o \
./obj/CUnit/Sources/TestRun.o \
./obj/CUnit/Sources/Util.o 

C_DEPS += \
./obj/CUnit/Sources/Automated.d \
./obj/CUnit/Sources/Basic.d \
./obj/CUnit/Sources/CUError.d \
./obj/CUnit/Sources/Console.d \
./obj/CUnit/Sources/MyMem.d \
./obj/CUnit/Sources/TestDB.d \
./obj/CUnit/Sources/TestRun.d \
./obj/CUnit/Sources/Util.d 


# Each subdirectory must supply rules for building sources it contributes
obj/CUnit/Sources/%.o: ../CUnit/Sources/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I"../CUnit/Headers" -I".." $(C_FLAGS) -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


