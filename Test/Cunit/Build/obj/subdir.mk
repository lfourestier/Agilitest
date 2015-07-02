################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../OperationsCTestSuite.c \
../main.c 

OBJS += \
./obj/OperationsCTestSuite.o \
./obj/main.o 

C_DEPS += \
./obj/OperationsCTestSuite.d \
./obj/main.d 


# Each subdirectory must supply rules for building sources it contributes
obj/%.o: ../%.c
	@echo "Building file: $<"
	@echo "Invoking: GCC C Compiler"
	gcc -I"../CUnit/Headers" -I".." $(C_FLAGS) -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo "Finished building: $<"
	@echo " "


