################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../OperationsCppTestSuite.cpp \
../main.cpp 

OBJS += \
./obj/OperationsCppTestSuite.o \
./obj/main.o 

CPP_DEPS += \
./obj/OperationsCppTestSuite.d \
./obj/main.d 


# Each subdirectory must supply rules for building sources it contributes
obj/%.o: ../%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I".." -I"../Gtest/include" -I"../Gtest" $(CPP_FLAGS) -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


