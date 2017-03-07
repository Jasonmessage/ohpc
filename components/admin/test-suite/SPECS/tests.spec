#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %global PROJ_DELIM -ohpc}

Summary:   Integration test stuie for OpenHPC
Name:      test-suite%{PROJ_DELIM}
Version:   1.3
Release:   1
License:   Apache-2.0
Group:     %{PROJ_NAME}/admin
BuildArch: noarch
URL:       https://github.com/openhpc/ohpc/tests
Source0:   tests-ohpc.tar
Source1:   OHPC_macros

BuildRequires:  autoconf%{PROJ_DELIM}
BuildRequires:  automake%{PROJ_DELIM}

%if 0%{?suse_version} >= 1230
Requires(pre):  shadow
%endif

BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root
DocDir:    %{OHPC_PUB}/doc/contrib

%define testuser ohpc-test
%define debug_package %{nil}

%description

This package provides a suite of integration tests used by the OpenHPC project
during continuous integration. Most components can be tested individually, but
a default configuration is setup to enable collective testing. The test suite
is made available under an 'ohpctest' user account.

%prep
%setup -n tests-ohpc

%build

export PATH=/opt/ohpc/pub/autotools/bin:$PATH
cd tests
./bootstrap


%install

cd tests
%{__mkdir_p} %{buildroot}/home/%{testuser}/tests
cp -a * %{buildroot}/home/%{testuser}/tests
find %{buildroot}/home/%{testuser}/tests -name .gitignore  -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%pre
getent passwd %{testuser} >/dev/null || \
    /usr/sbin/useradd -U -c "OpenHPC integration test account" \
    -s /bin/bash -m -b /home %{testuser}
exit 0

%post

%postun


%files
%defattr(-,%{testuser},%{testuser},-)
%dir /home/%{testuser}
/home/%{testuser}/tests



