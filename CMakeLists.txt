# Minimum CMake version
cmake_minimum_required(VERSION 3.10)

# Project name
project(base_app)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 14)

# Add the executable (main application)
add_executable(base_app src/main.cpp src/helper.cpp)
