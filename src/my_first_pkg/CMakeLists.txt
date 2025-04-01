cmake_minimum_required(VERSION 3.8)
project(my_first_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(
  PROGRAMS
    my_first_pkg/talker_py.py
    my_first_pkg/listener_py.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
