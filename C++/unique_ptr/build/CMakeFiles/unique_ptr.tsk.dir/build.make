# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.22.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.22.2/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/jimyang/projects/algorithms/C++/unique_ptr

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/jimyang/projects/algorithms/C++/unique_ptr/build

# Include any dependencies generated for this target.
include CMakeFiles/unique_ptr.tsk.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/unique_ptr.tsk.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/unique_ptr.tsk.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/unique_ptr.tsk.dir/flags.make

CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o: CMakeFiles/unique_ptr.tsk.dir/flags.make
CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o: ../unique_ptr.m.cpp
CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o: CMakeFiles/unique_ptr.tsk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/jimyang/projects/algorithms/C++/unique_ptr/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o -MF CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o.d -o CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o -c /Users/jimyang/projects/algorithms/C++/unique_ptr/unique_ptr.m.cpp

CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/jimyang/projects/algorithms/C++/unique_ptr/unique_ptr.m.cpp > CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.i

CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/jimyang/projects/algorithms/C++/unique_ptr/unique_ptr.m.cpp -o CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.s

# Object files for target unique_ptr.tsk
unique_ptr_tsk_OBJECTS = \
"CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o"

# External object files for target unique_ptr.tsk
unique_ptr_tsk_EXTERNAL_OBJECTS =

unique_ptr.tsk: CMakeFiles/unique_ptr.tsk.dir/unique_ptr.m.cpp.o
unique_ptr.tsk: CMakeFiles/unique_ptr.tsk.dir/build.make
unique_ptr.tsk: CMakeFiles/unique_ptr.tsk.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/jimyang/projects/algorithms/C++/unique_ptr/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable unique_ptr.tsk"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/unique_ptr.tsk.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/unique_ptr.tsk.dir/build: unique_ptr.tsk
.PHONY : CMakeFiles/unique_ptr.tsk.dir/build

CMakeFiles/unique_ptr.tsk.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/unique_ptr.tsk.dir/cmake_clean.cmake
.PHONY : CMakeFiles/unique_ptr.tsk.dir/clean

CMakeFiles/unique_ptr.tsk.dir/depend:
	cd /Users/jimyang/projects/algorithms/C++/unique_ptr/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/jimyang/projects/algorithms/C++/unique_ptr /Users/jimyang/projects/algorithms/C++/unique_ptr /Users/jimyang/projects/algorithms/C++/unique_ptr/build /Users/jimyang/projects/algorithms/C++/unique_ptr/build /Users/jimyang/projects/algorithms/C++/unique_ptr/build/CMakeFiles/unique_ptr.tsk.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/unique_ptr.tsk.dir/depend

