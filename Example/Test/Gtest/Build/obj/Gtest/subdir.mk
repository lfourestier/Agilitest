################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../Gtest/gtest-all.cc 

OBJS += \
./obj/Gtest/gtest-all.o 

CC_DEPS += \
./obj/Gtest/gtest-all.d 


# Each subdirectory must supply rules for building sources it contributes
obj/Gtest/%.o: ../Gtest/%.cc
	@echo "Building file: $<"
	@echo "Invoking: GCC C++ Compiler"
	g++ -I"../Gtest/src" -I"../Gtest/include" -I"../Gtest" $(CPP_FLAGS) -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo "Finished building: $<"
	@echo " "


