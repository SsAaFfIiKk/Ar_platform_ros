cmake_minimum_required(VERSION 3.0.2)
project(platform)

find_package(
  catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)



add_message_files(
  FILES
  Point2d.msg
  MarkerData.msg
  ArucoData.msg
)

generate_messages(
   DEPENDENCIES
   std_msgs
 )

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES platform
  CATKIN_DEPENDS message_runtime roscpp rospy std_msgs
#  DEPENDS system_lib
)



include_directories(
  ${catkin_INCLUDE_DIRS}
)

