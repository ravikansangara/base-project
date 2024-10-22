# Minimum CMake version
cmake_minimum_required(VERSION 3.10)

# Project name
project(base_app)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 14)

# Add submodules
add_subdirectory(submodules/module-one)
add_subdirectory(submodules/module-two)

# Add the executable (main application)
add_executable(base_app src/main.cpp src/helper.cpp)

# Specify the include directories
target_include_directories(base_app PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/submodules/module-one/src)
target_include_directories(base_app PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/submodules/module-two/src)

# Link the static library from the submodule to the main project
target_link_libraries(base_app PRIVATE one)
target_link_libraries(base_app PRIVATE two)