################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../src/Gtest/gtest-all.cc 

OBJS += \
./src/Gtest/gtest-all.o 

CC_DEPS += \
./src/Gtest/gtest-all.d 


# Each subdirectory must supply rules for building sources it contributes
src/Gtest/%.o: ../src/Gtest/%.cc
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I"/home/luc/Projects/Sandbox/CIEnvironment/Test/Gtest/src/Gtest/include" -I"/home/luc/Projects/Sandbox/CIEnvironment/Test/Gtest/src/Gtest" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


