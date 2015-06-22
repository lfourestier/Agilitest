################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../src/Gtest/src/gtest-all.cc \
../src/Gtest/src/gtest-death-test.cc \
../src/Gtest/src/gtest-filepath.cc \
../src/Gtest/src/gtest-port.cc \
../src/Gtest/src/gtest-printers.cc \
../src/Gtest/src/gtest-test-part.cc \
../src/Gtest/src/gtest-typed-test.cc \
../src/Gtest/src/gtest.cc 

OBJS += \
./src/Gtest/src/gtest-all.o \
./src/Gtest/src/gtest-death-test.o \
./src/Gtest/src/gtest-filepath.o \
./src/Gtest/src/gtest-port.o \
./src/Gtest/src/gtest-printers.o \
./src/Gtest/src/gtest-test-part.o \
./src/Gtest/src/gtest-typed-test.o \
./src/Gtest/src/gtest.o 

CC_DEPS += \
./src/Gtest/src/gtest-all.d \
./src/Gtest/src/gtest-death-test.d \
./src/Gtest/src/gtest-filepath.d \
./src/Gtest/src/gtest-port.d \
./src/Gtest/src/gtest-printers.d \
./src/Gtest/src/gtest-test-part.d \
./src/Gtest/src/gtest-typed-test.d \
./src/Gtest/src/gtest.d 


# Each subdirectory must supply rules for building sources it contributes
src/Gtest/src/%.o: ../src/Gtest/src/%.cc
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I"/home/luc/Projects/Sandbox/CIEnvironment/Test/Gtest/src/Gtest/include" -I"/home/luc/Projects/Sandbox/CIEnvironment/Test/Gtest/src/Gtest" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


