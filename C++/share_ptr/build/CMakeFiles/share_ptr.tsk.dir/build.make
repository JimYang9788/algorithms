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
CMAKE_SOURCE_DIR = /Users/jimyang/Projects/algorithms/C++/share_ptr

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/jimyang/Projects/algorithms/C++/share_ptr/build

# Include any dependencies generated for this target.
include CMakeFiles/share_ptr.tsk.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/share_ptr.tsk.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/share_ptr.tsk.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/share_ptr.tsk.dir/flags.make

CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o: CMakeFiles/share_ptr.tsk.dir/flags.make
CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o: ../share_ptr.m.cpp
CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o: CMakeFiles/share_ptr.tsk.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/jimyang/Projects/algorithms/C++/share_ptr/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o -MF CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o.d -o CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o -c /Users/jimyang/Projects/algorithms/C++/share_ptr/share_ptr.m.cpp

CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/jimyang/Projects/algorithms/C++/share_ptr/share_ptr.m.cpp > CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.i

CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/jimyang/Projects/algorithms/C++/share_ptr/share_ptr.m.cpp -o CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.s

# Object files for target share_ptr.tsk
share_ptr_tsk_OBJECTS = \
"CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o"

# External object files for target share_ptr.tsk
share_ptr_tsk_EXTERNAL_OBJECTS =

share_ptr.tsk: CMakeFiles/share_ptr.tsk.dir/share_ptr.m.cpp.o
share_ptr.tsk: CMakeFiles/share_ptr.tsk.dir/build.make
share_ptr.tsk: CMakeFiles/share_ptr.tsk.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/jimyang/Projects/algorithms/C++/share_ptr/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable share_ptr.tsk"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/share_ptr.tsk.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/share_ptr.tsk.dir/build: share_ptr.tsk
.PHONY : CMakeFiles/share_ptr.tsk.dir/build

CMakeFiles/share_ptr.tsk.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/share_ptr.tsk.dir/cmake_clean.cmake
.PHONY : CMakeFiles/share_ptr.tsk.dir/clean

CMakeFiles/share_ptr.tsk.dir/depend:
	cd /Users/jimyang/Projects/algorithms/C++/share_ptr/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/jimyang/Projects/algorithms/C++/share_ptr /Users/jimyang/Projects/algorithms/C++/share_ptr /Users/jimyang/Projects/algorithms/C++/share_ptr/build /Users/jimyang/Projects/algorithms/C++/share_ptr/build /Users/jimyang/Projects/algorithms/C++/share_ptr/build/CMakeFiles/share_ptr.tsk.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/share_ptr.tsk.dir/depend

