Name:		liblivebox-service
Version:	0.5.6
Release:	1
License:	Flora
Summary:	Service API for gathering installed livebox information
Group:		HomeTF/Livebox
Source0:	%{name}-%{version}.tar.gz
Source1001:	%{name}.manifest
BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	gettext-tools
BuildRequires:	pkgconfig(dlog)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(com-core)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(db-util)
BuildRequires:	pkgconfig(pkgmgr)
BuildRequires:	pkgconfig(pkgmgr-info)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(vconf)
BuildRequires:	pkgconfig(ail)
BuildRequires:	pkgconfig(icu-uc)

%description
Service API for gathering information of installed liveboxes

%package devel
Summary:	Files for livebox service
Requires:	%{name} = %{version}-%{release}

%description devel
Gathering the installed livebox information.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%if 0%{?tizen_build_binary_release_type_eng}
export CFLAGS="${CFLAGS} -DTIZEN_ENGINEER_MODE"
export CXXFLAGS="${CXXFLAGS} -DTIZEN_ENGINEER_MODE"
export FFLAGS="${FFLAGS} -DTIZEN_ENGINEER_MODE"
%endif
%cmake .
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/%{_datarootdir}/license

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -n liblivebox-service
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_datarootdir}/license/*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/livebox-service/livebox-service.h
%{_includedir}/livebox-service/livebox-errno.h
%{_libdir}/pkgconfig/*.pc

# End of a file
