#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
#

AC_PREREQ(2.59)
AC_INIT([cilk], [2.0], [https://github.com/openhpc/ohpc])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

# verify we have necessary environment variables set

OHPC_COMPILER_FAMILY

# Define include path and library linkage from environment variables
# which should be provided via module loads. 

CFLAGS="-I${TBBROOT}/include ${CFLAGS}"
CXXFLAGS="-I${TBBROOT}/include ${CXXFLAGS}"
LDFLAGS="-L${TBBROOT}/lib ${LDFLAGS}"
LIBS="-tbb -pthread ${LIBS}"

# test compilers
AC_PROG_CC
AC_PROG_CXX

# Set subdirectories
AC_CONFIG_FILES(Makefile tests/Makefile)

# Configure
AC_OUTPUT()

echo
echo '-------------------------------------------------- SUMMARY --------------------------------------------------'
echo
echo Package version............... : $PACKAGE-$VERSION
echo OHPC compiler toolchain........ : $LMOD_FAMILY_COMPILER
echo
echo C compiler.................... : `which $CC`
echo C++ compiler.................. : `which $CXX`
echo 
echo C compiler flags.............. : $CFLAGS
echo C++ compiler flags............ : $CXXFLAGS
echo Linker flags.................. : $LDFLAGS $LIBS
echo 
echo '-------------------------------------------------------------------------------------------------------------'
