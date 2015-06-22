################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/GtestTestSuite.cpp \
../src/SecondTestSuite.cpp \
../src/main.cpp 

OBJS += \
./src/GtestTestSuite.o \
./src/SecondTestSuite.o \
./src/main.o 

CPP_DEPS += \
./src/GtestTestSuite.d \
./src/SecondTestSuite.d \
./src/main.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I"/home/luc/Projects/Sandbox/CIEnvironment/Test/Gtest/src/Gtest/include" -I"/home/luc/Projects/Sandbox/CIEnvironment/Test/Gtest/src/Gtest" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


