# $Id$
# Authority dries

%global scl_name_prefix scld-
%global scl_name_base boost
%global scl_name_version 162

%global scl %{scl_name_prefix}%{scl_name_base}%{scl_name_version}

%global nfsmountable 1

%scl_package %scl
%global _scl_prefix /opt/dries

Summary: Package that installs %scl
Name: %scl_name
Version: 1
Release: 1%{?dist}
License: GPLv2+
Requires: %{scl_prefix}less
BuildRequires: scl-utils-build

%description
This is the main package for %scl Software Collection.

%package runtime
Summary: Package that handles %scl Software Collection.
Requires: scl-utils

%description runtime
Package shipping essential scripts to work with %scl Software Collection.

%package build
Summary: Package shipping basic build configuration
Requires: scl-utils-build

%description build
Package shipping essential configuration macros to build %scl Software Collection.

# This is only needed when you want to provide an optional scldevel subpackage
%package scldevel
Summary: Package shipping development files for %scl

%description scldevel
Package shipping development files, especially useful for development of
packages depending on %scl Software Collection.

%prep
%setup -c -T

%install
%scl_install

cat >> %{buildroot}%{_scl_scripts}/enable << EOF
export PATH=%{_bindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\$MANPATH
export PKG_CONFIG_PATH=%{_libdir}/pkgconfig\${PKG_CONFIG_PATH:+:\${PKG_CONFIG_PATH}}
EOF

# This is only needed when you want to provide an optional scldevel subpackage
cat >> %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel << EOF
%%scl_%{scl_name_base} %{scl}
%%scl_prefix_%{scl_name_base} %{scl_prefix}
EOF

mkdir -p %{buildroot}%{_scl_prefix}
# Install the generated man page
#mkdir -p %{buildroot}%{_mandir}/man7/
#install -p -m 644 %{scl_name}.7 %{buildroot}%{_mandir}/man7/

%files

%files runtime -f filelist
%scl_files

%files build
%{_root_sysconfdir}/rpm/macros.%{scl}-config

%files scldevel
%{_root_sysconfdir}/rpm/macros.%{scl_name_base}-scldevel

%changelog
* Sat Dec 3 2016 Dries Verachtert <dries.verachtert@dries.eu> - 1.1
- Initial package, based on example at 
  https://www.softwarecollections.org/en/docs/guide/#sect-Creating_a_Meta_Package
